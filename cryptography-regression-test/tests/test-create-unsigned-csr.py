#!/usr/bin/python3

import unittest
from OpenSSL import crypto


class TestCryptography(unittest.TestCase):

    def _create_key_pair(self, type, bits):
        key_pair = crypto.PKey()
        key_pair.generate_key(type, bits)
        return key_pair

    def test_create_csr_that_has_not_been_signed(self):
        """Generate a CSR that has not been signed."""
        key_pair = self._create_key_pair(crypto.TYPE_RSA, 2048)
        csr = crypto.X509Req()
        subject = csr.get_subject()
        setattr(subject, "CN", "host.example.net")
        csr.set_pubkey(key_pair)
        pem = crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr)
        print(f"pem={pem}")
        return pem

if __name__ == '__main__':
    unittest.main()
