# -*- coding: utf-8 -*-
"""Aes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16tpF79HO996TpgJKmWaj0H7yXNfjBQZC

# Simple AES data tables
"""

# Defining a class containg the data tables
class data_tables:
  # table for substitution
  s_box = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
  ]
  # inverse for substitution table 
  inv_s_box = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
  ]
  # 
  r_con = [
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
  ]

"""# Simple AES functions used for encryption and decryption"""

# defining the function for conversion of text to matrix 
def Into_matrix(t):
  m = []
  for i in range(16):
      b = (t >> (8 * (15 - i)))
      b = b & 0xFF
      if i % 4 == 0:
          m.append([b])
      else:
          m[int(i / 4)].append(b)
  return m

# defining the function for conversion of matrix to text
def Into_text(matrix):
  t = 0
  for i in range(4):
      for j in range(4):
          t |= (matrix[i][j] << (120 - 8 * (4 * i + j)))
  return t

xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

# defining a class containing all the functions of aes encryption 
class aes_algorithm:
  # constructor function chainging the value of key provided at run time
  def __init__(self, key):
    self.modify_key(key)

  # function for chinging the keys for each round 
  def modify_key(self, key):
    self.rk = Into_matrix(key)
    print("Initially Enter key is:",hex(key),'\n')
    print("After conversion to matrix key is:",self.rk,'\n')

    for i in range(4, 4 * 11):
        self.rk.append([])
        if i % 4 == 0:
            b = self.rk[i - 4][0] ^ d.s_box[self.rk[i - 1][1]] ^ d.r_con[int(i / 4)]
            self.rk[i].append(b)

            for j in range(1, 4):
                b = self.rk[i - 4][j] ^ d.s_box[self.rk[i - 1][(j + 1) % 4]]
                self.rk[i].append(b)
        else:
             for j in range(4):
                b = self.rk[i - 4][j] ^ self.rk[i - 1][j]
                self.rk[i].append(b)
    print("Next key is:",hex(Into_text(self.rk)),'\n')

  # defining the function for adding the round keys
  def add_round_key(self, s, k):
        for i in range(4):
            for j in range(4):
                s[i][j] ^= k[i][j]

  # defining the function for defining the functions in one round of encryption
  def one_round_encrypt(self, state, key_matrix):
      self.substitution_bytes(state)
      self.rows_shift(state)
      self.mixcolumns(state)
      self.add_round_key(state, key_matrix)
      return state,key_matrix

  # defining the function for defining the functions in one round of decryption
  def one_round_decrypt(self, state, key_matrix):
      self.add_round_key(state, key_matrix)
      self.inverse_mixcolumns(state)
      self.inverse_rows_shift(state)
      self.inverse_substitution_bytes(state)
      return state,key_matrix
  
  # defining the function for sunstituting the bytes 
  def substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.s_box[s[i][j]]

  # defing the funtion for inverse substitution of bytes
  def inverse_substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.inv_s_box[s[i][j]]

  # defining the function for shifting operation
  def rows_shift(self, s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

  # defining the function for inverse shifting operation
  def inverse_rows_shift(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
  
  # defining the function for mix column operation
  def mixing_single_column(self, a):
    # please see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)

  # defining the mix columns operation
  def mixcolumns(self, s):
    for i in range(4):
        self.mixing_single_column(s[i])

  # defining the inverse of mix column operation
  def inverse_mixcolumns(self, s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v
    self.mixcolumns(s)

  # defining the encryption function
  def encryption(self, plaintext):
    print("For Encryption Process:\n")
    self.plain_state = Into_matrix(plaintext)
    self.add_round_key(self.plain_state, self.rk[:4])
    # for initial 10 rounds run all 4 operations 
    for i in range(1, 10):
      s,k = self.one_round_encrypt(self.plain_state, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",i,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    # for last round need not run mix_column operation
    self.substitution_bytes(self.plain_state)
    self.rows_shift(self.plain_state)
    self.add_round_key(self.plain_state, self.rk[40:])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.plain_state)

  # defining the encryption function
  def decryption(self, ciphertext):
    print("For Dencryption Process:\n")
    self.cipher = Into_matrix(ciphertext)
    self.add_round_key(self.cipher, self.rk[40:])
    self.inverse_rows_shift(self.cipher)
    self.inverse_substitution_bytes(self.cipher)
    j = 1
    for i in range(9, 0, -1):
      s,k = self.one_round_decrypt(self.cipher, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",j,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
      j = j + 1
    self.add_round_key(self.cipher, self.rk[:4])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.cipher)

"""# Modified AES algotithm"""

# defining a class containing all the functions of aes encryption with modified shift operation
class modified_aes_shift_algorithm:
  # constructor function chainging the value of key provided at run time
  def __init__(self, key):
    self.modify_key(key)

  # function for chinging the keys for each round 
  def modify_key(self, key):
    self.rk = Into_matrix(key)
    print("Initially Enter key is:",hex(key),'\n')
    print("After conversion to matrix key is:",self.rk,'\n')

    for i in range(4, 4 * 11):
        self.rk.append([])
        if i % 4 == 0:
            b = self.rk[i - 4][0] ^ d.s_box[self.rk[i - 1][1]] ^ d.r_con[int(i / 4)]
            self.rk[i].append(b)

            for j in range(1, 4):
                b = self.rk[i - 4][j] ^ d.s_box[self.rk[i - 1][(j + 1) % 4]]
                self.rk[i].append(b)
        else:
             for j in range(4):
                b = self.rk[i - 4][j] ^ self.rk[i - 1][j]
                self.rk[i].append(b)
    print("Next key is:",hex(Into_text(self.rk)),'\n')

  # defining the function for adding the round keys
  def add_round_key(self, s, k):
        for i in range(4):
            for j in range(4):
                s[i][j] ^= k[i][j]

  # defining the function for defining the functions in one round of encryption
  def one_round_encrypt(self, state, key_matrix):
      self.substitution_bytes(state)
      self.rows_shift(state)
      self.mixcolumns(state)
      self.add_round_key(state, key_matrix)
      return state,key_matrix

  # defining the function for defining the functions in one round of decryption
  def one_round_decrypt(self, state, key_matrix):
      self.add_round_key(state, key_matrix)
      self.inverse_mixcolumns(state)
      self.inverse_rows_shift(state)
      self.inverse_substitution_bytes(state)
      return state,key_matrix
  
  # defining the function for sunstituting the bytes 
  def substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.s_box[s[i][j]]

  # defing the funtion for inverse substitution of bytes
  def inverse_substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.inv_s_box[s[i][j]]

  # defining the function for shifting operation
  def rows_shift(self, s):
    s[0][0], s[1][0], s[2][0], s[3][0] = s[2][0], s[3][0], s[0][0], s[1][0]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[3][2], s[0][2], s[1][2], s[2][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

  # defining the function for inverse shifting operation
  def inverse_rows_shift(self, s):
        s[0][0], s[1][0], s[2][0], s[3][0] = s[2][0], s[3][0], s[0][0], s[1][0]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[1][2], s[2][2], s[3][2], s[0][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
  
  # defining the function for mix column operation
  def mixing_single_column(self, a):
    # please see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)

  # defining the mix columns operation
  def mixcolumns(self, s):
    for i in range(4):
        self.mixing_single_column(s[i])

  # defining the inverse of mix column operation
  def inverse_mixcolumns(self, s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v
    self.mixcolumns(s)

  # defining the encryption function
  def encryption(self, plaintext):
    print("For Encryption Process:\n")
    self.plain_state = Into_matrix(plaintext)
    self.add_round_key(self.plain_state, self.rk[:4])
    # for initial 10 rounds run all 4 operations 
    for i in range(1, 10):
      s,k = self.one_round_encrypt(self.plain_state, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",i,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    # for last round need not run mix_column operation
    self.substitution_bytes(self.plain_state)
    self.rows_shift(self.plain_state)
    self.add_round_key(self.plain_state, self.rk[40:])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.plain_state)

  # defining the encryption function
  def decryption(self, ciphertext):
    print("For Dencryption Process:\n")
    self.cipher = Into_matrix(ciphertext)
    self.add_round_key(self.cipher, self.rk[40:])
    self.inverse_rows_shift(self.cipher)
    self.inverse_substitution_bytes(self.cipher)
    j = 1
    for i in range(9, 0, -1):
      s,k = self.one_round_decrypt(self.cipher, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",j,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
      j = j + 1
    self.add_round_key(self.cipher, self.rk[:4])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.cipher)

# defining a class containing all the functions of aes encryption with modified xor which is xnor 
class modified_aes_xor_algorithm:
  # constructor function chainging the value of key provided at run time
  def __init__(self, key):
    self.modify_key(key)

  # function for chinging the keys for each round 
  def modify_key(self, key):
    self.rk = Into_matrix(key)
    print("Initially Enter key is:",hex(key),'\n')
    print("After conversion to matrix key is:",self.rk,'\n')

    for i in range(4, 4 * 11):
        self.rk.append([])
        if i % 4 == 0:
            b = 0xff - (self.rk[i - 4][0] ^ d.s_box[self.rk[i - 1][1]] ^ d.r_con[int(i / 4)])
            self.rk[i].append(b)

            for j in range(1, 4):
                b = 0xff - (self.rk[i - 4][j] ^ d.s_box[self.rk[i - 1][(j + 1) % 4]])
                self.rk[i].append(b)
        else:
             for j in range(4):
                b = 0xff - (self.rk[i - 4][j] ^ self.rk[i - 1][j])
                self.rk[i].append(b)
    print("Next key is:",hex(Into_text(self.rk)),'\n')

  # defining the function for adding the round keys
  def add_round_key(self, s, k):
        for i in range(4):
            for j in range(4):
                s[i][j] = 0xff - (s[i][j] ^ k[i][j])

  # defining the function for defining the functions in one round of encryption
  def one_round_encrypt(self, state, key_matrix):
      self.substitution_bytes(state)
      self.rows_shift(state)
      self.mixcolumns(state)
      self.add_round_key(state, key_matrix)
      return state,key_matrix

  # defining the function for defining the functions in one round of decryption
  def one_round_decrypt(self, state, key_matrix):
      self.add_round_key(state, key_matrix)
      self.inverse_mixcolumns(state)
      self.inverse_rows_shift(state)
      self.inverse_substitution_bytes(state)
      return state,key_matrix
  
  # defining the function for sunstituting the bytes 
  def substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.s_box[s[i][j]]

  # defing the funtion for inverse substitution of bytes
  def inverse_substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.inv_s_box[s[i][j]]

  # defining the function for shifting operation
  def rows_shift(self, s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

  # defining the function for inverse shifting operation
  def inverse_rows_shift(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
  
  # defining the function for mix column operation
  def mixing_single_column(self, a):
    # please see Sec 4.1.2 in The Design of Rijndael
    t = 0xff - (a[0] ^ a[1] ^ a[2] ^ a[3])
    u = a[0]
    a[0] = 0xff - (a[0] ^ t ^ xtime(a[0] ^ a[1]))
    a[1] = 0xff - (a[1] ^ t ^ xtime(a[1] ^ a[2]))
    a[2] = 0xff - (a[2] ^ t ^ xtime(a[2] ^ a[3]))
    a[3] = 0xff - (a[3] ^ t ^ xtime(a[3] ^ u))

  # defining the mix columns operation
  def mixcolumns(self, s):
    for i in range(4):
        self.mixing_single_column(s[i])

  # defining the inverse of mix column operation
  def inverse_mixcolumns(self, s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = 0xff - (xtime(xtime(s[i][0] ^ s[i][2])))
        v = 0xff - (xtime(xtime(s[i][1] ^ s[i][3])))
        s[i][0] = 0xff -(s[i][0] ^ u)
        s[i][1] = 0xff -(s[i][1] ^ v)
        s[i][2] = 0xff -(s[i][2] ^ u)
        s[i][3] = 0xff -(s[i][3] ^ v)
    self.mixcolumns(s)

  # defining the encryption function
  def encryption(self, plaintext):
    print("For Encryption Process:\n")
    self.plain_state = Into_matrix(plaintext)
    self.add_round_key(self.plain_state, self.rk[:4])
    # for initial 10 rounds run all 4 operations 
    for i in range(1, 10):
      s,k = self.one_round_encrypt(self.plain_state, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",i,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    # for last round need not run mix_column operation
    self.substitution_bytes(self.plain_state)
    self.rows_shift(self.plain_state)
    self.add_round_key(self.plain_state, self.rk[40:])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.plain_state)

  # defining the encryption function
  def decryption(self, ciphertext):
    print("For Dencryption Process:\n")
    self.cipher = Into_matrix(ciphertext)
    self.add_round_key(self.cipher, self.rk[40:])
    self.inverse_rows_shift(self.cipher)
    self.inverse_substitution_bytes(self.cipher)
    j = 1
    for i in range(9, 0, -1):
      s,k = self.one_round_decrypt(self.cipher, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",j,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
      j = j + 1
    self.add_round_key(self.cipher, self.rk[:4])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.cipher)

# defining a class containing all the functions of aes encryption with modified mix column operation 
class modified_aes_column_algorithm:
  # constructor function chainging the value of key provided at run time
  def __init__(self, key):
    self.modify_key(key)

  # function for chinging the keys for each round 
  def modify_key(self, key):
    self.rk = Into_matrix(key)
    print("Initially Enter key is:",hex(key),'\n')
    print("After conversion to matrix key is:",self.rk,'\n')

    for i in range(4, 4 * 11):
        self.rk.append([])
        if i % 4 == 0:
            b = self.rk[i - 4][0] ^ d.s_box[self.rk[i - 1][1]] ^ d.r_con[int(i / 4)]
            self.rk[i].append(b)

            for j in range(1, 4):
                b = self.rk[i - 4][j] ^ d.s_box[self.rk[i - 1][(j + 1) % 4]]
                self.rk[i].append(b)
        else:
             for j in range(4):
                b = self.rk[i - 4][j] ^ self.rk[i - 1][j]
                self.rk[i].append(b)
    print("Next key is:",hex(Into_text(self.rk)),'\n')

  # defining the function for adding the round keys
  def add_round_key(self, s, k):
        for i in range(4):
            for j in range(4):
                s[i][j] ^= k[i][j]

  # defining the function for defining the functions in one round of encryption
  def one_round_encrypt(self, state, key_matrix):
      self.substitution_bytes(state)
      self.rows_shift(state)
      self.mixcolumns(state)
      self.add_round_key(state, key_matrix)
      return state,key_matrix

  # defining the function for defining the functions in one round of decryption
  def one_round_decrypt(self, state, key_matrix):
      self.add_round_key(state, key_matrix)
      self.inverse_mixcolumns(state)
      self.inverse_rows_shift(state)
      self.inverse_substitution_bytes(state)
      return state,key_matrix
  
  # defining the function for sunstituting the bytes 
  def substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.s_box[s[i][j]]

  # defing the funtion for inverse substitution of bytes
  def inverse_substitution_bytes(self, s):
    for i in range(4):
        for j in range(4):
            s[i][j] = d.inv_s_box[s[i][j]]

  # defining the function for shifting operation
  def rows_shift(self, s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

  # defining the function for inverse shifting operation
  def inverse_rows_shift(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
  
  # defining the function for mix column operation
  def mixing_single_column(self, a):
    # please see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    r = a[1]
    s = a[2]
    y = a[3]
    a[1] ^= t ^ xtime(s ^ u)
    a[3] ^= t ^ xtime(r ^ s)
    a[0] ^= t ^ xtime(y ^ r)
    a[2] ^= t ^ xtime(u ^ y)

  # defining the mix columns operation
  def mixcolumns(self, s):
    for i in range(4):
        self.mixing_single_column(s[i])

  # defining the inverse of mix column operation
  def inverse_mixcolumns(self, s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][1]))
        v = xtime(xtime(s[i][2] ^ s[i][3]))
        s[i][0] ^= u
        s[i][2] ^= v
        s[i][1] ^= u
        s[i][3] ^= v
    self.mixcolumns(s)

  # defining the encryption function
  def encryption(self, plaintext):
    print("For Encryption Process:\n")
    self.plain_state = Into_matrix(plaintext)
    self.add_round_key(self.plain_state, self.rk[:4])
    # for initial 10 rounds run all 4 operations 
    for i in range(1, 10):
      s,k = self.one_round_encrypt(self.plain_state, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",i,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    # for last round need not run mix_column operation
    self.substitution_bytes(self.plain_state)
    self.rows_shift(self.plain_state)
    self.add_round_key(self.plain_state, self.rk[40:])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.plain_state)

  # defining the encryption function
  def decryption(self, ciphertext):
    print("For Dencryption Process:\n")
    self.cipher = Into_matrix(ciphertext)
    self.add_round_key(self.cipher, self.rk[40:])
    self.inverse_rows_shift(self.cipher)
    self.inverse_substitution_bytes(self.cipher)
    j = 1
    for i in range(9, 0, -1):
      s,k = self.one_round_decrypt(self.cipher, self.rk[4 * i : 4 * (i + 1)])
      print("For round:",j,'\n',"State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
      j = j + 1
    self.add_round_key(self.cipher, self.rk[:4])
    print("For last round:\n","State Matrix is:",s,'\n',"Converting state in text:",hex(Into_text(s)),'\n',"Key used is:",k,'\n',"Converting key in text:",hex(Into_text(k)),'\n')
    return Into_text(self.cipher)

"""# Simple AES example"""

file1 = open("input_q2.txt","r")
s = file1.read(16)
print("Entered Data is:\n",s)
plaintext = int(s.encode('utf-8').hex(),16)
k = int(input("Enter 16 dight key:\n").encode('utf-8').hex(),16)

d = data_tables()
aes = aes_algorithm(k)
encrypted = aes.encryption(plaintext)
print("Encrypted text:",hex(encrypted))
decrypted = aes.decryption(encrypted)
print("Decrypted text:",hex(decrypted))
print("Plaintext:",hex(plaintext))
simple = hex(encrypted)[2:]

file2 = open("output_q2.txt","w+")
file2.write("For Simple AES\n")
data_ = "Cipher text is:"+hex(encrypted)[2:]+'\n'
file2.write(data_)
"""# Modifed AES example"""

d = data_tables()
modified = []
x = 'y'
while x == 'y':
  m = input("AES Algortihm:\n1. Modified AES Shift row\n2. Modified AES xor\n3. Modified AES column mixing\n")
  if m == "1":
    print("For Modified shift AES:\n")
    aes = modified_aes_shift_algorithm(k)
  elif m == "2":
    print("For Modified Xor AES:\n")
    aes = modified_aes_xor_algorithm(k)
  elif m == "3":
    print("For Modified Column Mix AES:\n")
    aes = modified_aes_column_algorithm(k)
  else:
    print("Wrong Choice...!!!")
    break
  encrypted = aes.encryption(plaintext)
  print("Encrypted text:",hex(encrypted))
  decrypted = aes.decryption(encrypted)
  print("Decrypted text:",hex(decrypted))
  print("Plaintext:",hex(plaintext))
  modified=(hex(encrypted)[2:])
  file2.write("For Modified AES\n")
  data_ = "Cipher text is:"+hex(encrypted)[2:]+'\n'
  file2.write(data_)
  """# Calculating Avalanche Effect"""
  print("For avalanche effect")
  count = 0
  for i in range(len(simple)):
    if simple[i] != modified[i]:
      count = count + 1
  print("Simple AES cipher text is:",simple,'\n')
  print("Modified AES cipher text is:",modified,'\n')
  print("No. of different characters are:",count,'\n')
  print("Avalanche effect is:",count/len(simple)*100,'\n')
  x = input("Do you want to continue...y/n\n")
