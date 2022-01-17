# cryptography-regression-test

To run tests with upstream Python (note success):
```
tox -e py39
tox -e py310
```

To run against distro package (note failure):
```
apt install python3-openssl

cryptography-regression-test$ ./cryptography-regression-test/tests/test-create-unsigned-csr.py

======================================================================
ERROR: test_create_csr_that_has_not_been_signed (__main__.TestCryptography)
Generate a CSR that has not been signed.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/tmp/cryptography-regression-test/./cryptography-regression-test/tests/test-create-unsigned-csr.py", line 21, in test_create_csr_that_has_not_been_signed
    pem = crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr)
  File "/usr/lib/python3/dist-packages/OpenSSL/crypto.py", line 2969, in dump_certificate_request
    _openssl_assert(result_code != 0)
  File "/usr/lib/python3/dist-packages/OpenSSL/_util.py", line 71, in openssl_assert
    exception_from_error_queue(error)
  File "/usr/lib/python3/dist-packages/OpenSSL/_util.py", line 57, in exception_from_error_queue
    raise exception_type(errors)
OpenSSL.crypto.Error: [('asn1 encoding routines', '', 'illegal zero content'), ('PEM routines', '', 'ASN1 lib')]

----------------------------------------------------------------------
Ran 1 test in 0.083s

FAILED (errors=1)
```
