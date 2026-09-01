#----------------------------------------------------------#
#        Program: Smartcard Example 2025/10/01             #
#               All rights reserved 2025                   #
#----------------------------------------------------------#
#     From: Ekobots Innovation Ltda - www.ekobots.com      #
#       by: Juan Sirgado y Antico - www.jsya.com           #
#----------------------------------------------------------#
# Description: Read SmartCard                              # 
#----------------------------------------------------------#
# Command/List of Libs pre-requisite:                      #
# pip install pyscard                                      #
#----------------------------------------------------------#
from smartcard.System import readers
from smartcard.util import toHexString, toBytes
from smartcard.Exceptions import NoCardException, CardConnectionException
#----------------------------------------------------------#
def list_readers():
    r = readers()
    print("Readers found:")
    for i, rr in enumerate(r):
        print(f"  [{i}] {rr}")
    return r
#----------------------------------------------------------#
def connect_to_reader(reader):
    """ Connect to a card on the given reader (reader is reader object or index) """
    try:
        if isinstance(reader, int):
            r = readers()[reader]
        else:
            r = reader
        conn = r.createConnection()
        conn.connect()  # Default protocol (T=0 or T=1) chosen automatically
        return conn
    except IndexError:
        raise RuntimeError("No such reader index")
    except NoCardException:
        raise RuntimeError("No card present in the reader")
    except CardConnectionException as e:
        raise RuntimeError(f"Could not connect to card: {e}")
#----------------------------------------------------------#
def get_atr(conn):
    atr = conn.getATR()
    print("ATR:", toHexString(atr))
    return atr
#----------------------------------------------------------#
def send_apdu(conn, apdu):
    """
    Send an APDU (list/bytes) and return (data_bytes, sw1, sw2)
    Example APDU format: [0x00, 0xA4, 0x04, 0x00, 0x07, ...]
    """
    print("=> APDU:", toHexString(apdu))
    resp, sw1, sw2 = conn.transmit(apdu)
    print("<= Response:", toHexString(resp), f"SW1={hex(sw1)} SW2={hex(sw2)}")
    return resp, sw1, sw2
#----------------------------------------------------------#
def get_uid(conn):
    """
    Common vendor-support GET UID APDU for many PC/SC readers:
      FF CA 00 00 00
    This is not an ISO7816 standard APDU, but many readers implement it.
    """
    apdu = [0xFF, 0xCA, 0x00, 0x00, 0x00]
    try:
        resp, sw1, sw2 = send_apdu(conn, apdu)
        if (sw1, sw2) == (0x90, 0x00) or sw1 == 0x61:
            # 0x90 0x00 success, 0x61 xx may indicate response available
            return bytes(resp)
        else:
            print("UID command returned status:", hex(sw1), hex(sw2))
            return None
    except Exception as e:
        print("Error sending UID APDU:", e)
        return None
#----------------------------------------------------------#
def select_aid(conn, aid_bytes):
    """SELECT by AID (ISO7816) - example returns response and status."""
    lc = len(aid_bytes)
    apdu = [0x00, 0xA4, 0x04, 0x00, lc] + list(aid_bytes)
    return send_apdu(conn, apdu)
#----------------------------------------------------------#
def read_binary_example(conn, offset=0, le=0x00):
    """
    READ BINARY using short APDU. offset can be 0..0x7FFF (for short).
    Here we show a short read binary example for a simple file.
    """
    p1 = (offset >> 8) & 0x7F  # high offset
    p2 = offset & 0xFF         # low offset
    apdu = [0x00, 0xB0, p1, p2, le]
    return send_apdu(conn, apdu)
#----------------------------------------------------------#
def main():
    try:
        rlist = list_readers()
        if not rlist:
            print("No PC/SC readers found. Is pcscd/PC/SC installed and running?")
            return

        # Choose first reader by default; change index if you want a specific one
        reader_index = 0
        print(f"\nUsing reader [{reader_index}]: {rlist[reader_index]}\n")

        conn = connect_to_reader(reader_index)
        atr = get_atr(conn)

        # Try to get UID (common vendor-level APDU)
        uid = get_uid(conn)
        if uid:
            print("UID (hex):", uid.hex().upper())
        else:
            print("Could not read UID with FF CA. Reader/card may not support that command.")

        # Example: select EMV payment AID (example A0000000031010)
        emv_aid = bytes.fromhex("A0000000031010")
        print("\nSelecting EMV AID (example):")
        select_resp = select_aid(conn, emv_aid)  # you can inspect response & SW

        # Example: attempt a short READ BINARY at offset 0 (may fail for many cards)
        print("\nAttempting READ BINARY (offset 0):")
        read_binary_example(conn, offset=0, le=0x00)

    except Exception as e:
        print("Error:", e)
#----------------------------------------------------------#
if __name__ == "__main__":
    main()
#----------------------------------------------------------#
# That is all folks!                                       #
#----------------------------------------------------------#