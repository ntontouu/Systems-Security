import hashlib
import hmac
import os
#ΜΕΡΟΣ 1Ο
def calculate_file_hash(file_path, algorithm='sha256'):
    try:
        hash_obj = hashlib.new(algorithm)#ΚΑΙΝΟΥΡΓΙΟ ΑΝΤΚΕΙΜΕΝΟ HASH K ALG ΟΤΙ ΕΒΑΛΕ ΑΠΟ ΜΑΙΝ
        with open(file_path, 'rb') as f: #ΔΙΑΒΆΖΕΙ ΤΟ ΑΡΧΕΙΟ ΣΕ BINARY
            for chunk in iter(lambda: f.read(65536), b''): #ΣΕ 64ΚΒ ΑΝΑ ΛΟΥΠΑ ΜΕΧΡΙ ΚΕΝΟ 
                hash_obj.update(chunk)#ΚΑΘΕ ΝΕΟ ΤΟ ΒΑΖΕΙ ΕΔΩ
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Σφάλμα κατά τον υπολογισμό hash: {e}")
        return None
#ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΣΥΓΚΡΙΣΗ, ΕΤΣΙ ΓΙΑ ΝΑ ΜΗΝ ΧΑΘΕΙ ΤΠΤ ΛΟΓΟ ΕΠΙΘΕΣΕΩΝ ΧΡΟΝΟΥ
def secure_hash_compare(hash1, hash2):
    '''
    ΤΑ ΚΑΝΕΙ ΟΛΑ ΠΕΖΑ ΓΙΑ ΝΑ ΜΗΝ ΕΧΕΙ ΘΕΜΑ ΣΤΗΝ ΣΥΓΚΡΙΣΗ
    ΚΡΑΤΑΕΙ ΣΤΑΘΕΡΟ ΧΡΟΝΟ ΑΦΟΥ ΗΜΑΚ, ΠΙΟ ΠΟΛΥ ΑΣΦΑΛΕΙΑ ΘΑ ΜΠΟΡΟΥΣΕ Κ == ΑΛΛΑ ΠΑΙΖΕΙ ΕΠΙΘΕΣΗ
    '''

    return hmac.compare_digest(hash1.lower(), hash2.lower())

#ΜΕΡΟΣ 2Ο
def verify_file_integrity(original_hash, current_hash):
    """
    Ελέγχει αν μια αρχική hash τιμή ταιριάζει με την τρέχουσα.

    Args:
        original_hash (str): Η αρχική hash τιμή
        current_hash (str): Η τρέχουσα hash τιμή

    Returns:
        bool: True αν ταιριάζουν, False διαφορετικά
    """
    if not original_hash or not current_hash:
        return False
    return secure_hash_compare(original_hash, current_hash)
#ΜΕΡΟΣ 3ο
def main():

    while True:
        print("\nΜενού Επιλογών:")
        print("1. Υπολογισμός hash τιμής αρχείου")
        print("2. Επαλήθευση ακεραιότητας αρχείου")
        print("3. Έξοδος")

        choice = input("Επιλέξτε ενέργεια (1-3): ")

        if choice == '1':
            algorithms = {
                '1': 'md5',
                '2': 'sha1',
                '3': 'sha256',
                '4': 'sha3_256'
            }
            print("\nΕπιλέξτε αλγόριθμο:")
            print("1. MD5")
            print("2. SHA-1")
            print("3. SHA-256")
            print("4. SHA3-256")
            alg_choice = input("Επιλογή (1-4): ")

            algorithm = algorithms.get(alg_choice, 'sha256')
            file_path = input("Εισάγετε τη διαδρομή του αρχείου: ")

            if not os.path.exists(file_path):
                print("Το αρχείο δεν υπάρχει.")
                continue

            file_hash = calculate_file_hash(file_path, algorithm)
            if file_hash:
                print(f"\nΗ τιμή hash ({algorithm}) είναι: {file_hash}")

        elif choice == '2':
            file_path = input("Εισάγετε τη διαδρομή του αρχείου: ")
            if not os.path.exists(file_path):
                print("Το αρχείο δεν υπάρχει.")
                continue

            original_hash = input("Εισάγετε τη γνωστή hash τιμή: ").strip()

            algorithms = {
                '1': 'md5',
                '2': 'sha1',
                '3': 'sha256',
                '4': 'sha3_256'
            }
            print("\nΕπιλέξτε αλγόριθμο (πρέπει να είναι ίδιος με τον αρχικό):")
            print("1. MD5")
            print("2. SHA-1")
            print("3. SHA-256")
            print("4. SHA3-256")
            alg_choice = input("Επιλογή (1-4): ")

            algorithm = algorithms.get(alg_choice, 'sha256')

            current_hash = calculate_file_hash(file_path, algorithm)

            if current_hash:
                if verify_file_integrity(original_hash, current_hash):
                    print("\nΤο αρχείο είναι ακέραιο! Οι hash τιμές ταιριάζουν.")
                else:
                    print("\nΤο αρχείο έχει τροποποιηθεί! Οι hash τιμές διαφέρουν.")

        elif choice == '3':
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε 1-3.")

if __name__ == "__main__":
    main()