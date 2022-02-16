# Defining a class that provides all utility functions required for des
class simple_des:
  # Hexadecimal to binary conversion
  def hexadecimal_to_binary(self,s):
    return str(bin(int(s,16)))[2:].zfill(64)

  # Binary to hexadecimal conversion
  def binary_to_hexadecimal(self,s):
    return hex(int(s,2))

  # Binary to decimal conversion
  def binary_to_decimal(self,binary):
    n = binary
    d , r , i  = 0 , 0 , 0 
    while n!=0:
      r = n % 10
      d = d + r * pow(2,i)
      n = n//10
      i = i + 1    
    return d

  # Decimal to binary conversion
  def decimal_to_binary(self,num):
    r = bin(num).replace("0b", "")
    if(len(r)%4 != 0):
      d = int(len(r) / 4)
      c = (4 * (d + 1)) - len(r)
      for i in range(0, c):
        r = '0' + r
    return r

  # permutation function to rearrange the bits
  def permutation(self,k, arr, n):
    permutation = ""
    for i in range(0, n):
      permutation = permutation + k[arr[i] - 1]
    return permutation

  # shifting the bits towards left by nth shifts
  def shift_left(self,k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
      s = k[1:len(k)] + k[0]
      k = s
      s = ""
    return k
    
  # calculating xor of two strings of binary number a and b
  def xor(self,a, b):
    ans = ""
    for i in range(len(a)):
      if a[i] == b[i]:
        ans = ans + "0"
      else:
        ans = ans + "1"
    return ans

# class defined for functions of modified des xor operation
class modified_des_xor:

  # Hexadecimal to binary conversion
  def hexadecimal_to_binary(self,s):
    return str(bin(int(s,16)))[2:].zfill(64)

  # Binary to hexadecimal conversion
  def binary_to_hexadecimal(self,s):
    return hex(int(s,2))

  # Binary to decimal conversion
  def binary_to_decimal(self,binary):
    n = binary
    d , r , i  = 0 , 0 , 0 
    while n!=0:
      r = n % 10
      d = d + r * pow(2,i)
      n = n//10
      i = i + 1    
    return d

  # Decimal to binary conversion
  def decimal_to_binary(self,num):
    r = bin(num).replace("0b", "")
    if(len(r)%4 != 0):
      d = int(len(r) / 4)
      c = (4 * (d + 1)) - len(r)
      for i in range(0, c):
        r = '0' + r
    return r

  # permutation function to rearrange the bits
  def permutation(self,k, arr, n):
    permutation = ""
    for i in range(0, n):
      permutation = permutation + k[arr[i] - 1]
    return permutation

  # shifting the bits towards left by nth shifts
  def shift_left(self,k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
      s = k[1:len(k)] + k[0]
      k = s
      s = ""
    return k
    
  # calculating xor of two strings of binary number a and b
  def xor(self,a, b):
    ans = ""
    for i in range(len(a)):
      if a[i] == b[i]:
        ans = ans + "1"
      else:
        ans = ans + "0"
    return ans


# Class containing the des data tables
class simple_data:
  # Initial Permutation Table
  initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

  # Expansion D-box Table
  expansion_d_box = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
      6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
      12, 13, 12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25, 24, 25, 26, 27,
      28, 29, 28, 29, 30, 31, 32, 1 ]

  # Straight Permutation Table
  per = [ 16, 7, 20, 21,
      29, 12, 28, 17,
      1, 15, 23, 26,
      5, 18, 31, 10,
      2, 8, 24, 14,
      32, 27, 3, 9,
      19, 13, 30, 6,
      22, 11, 4, 25 ]

  # S-box Table
  s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
        
      [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

      [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
    
      [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
      
      [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
    
      [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
      
      [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
      
      [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

  # Final Permutation Table
  final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25 ]

  # parity bit drop table
  keyp = [57, 49, 41, 33, 25, 17, 9,
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36,
      63, 55, 47, 39, 31, 23, 15,
      7, 62, 54, 46, 38, 30, 22,
      14, 6, 61, 53, 45, 37, 29,
      21, 13, 5, 28, 20, 12, 4 ]



  # Number of bit shifts
  shift_table = [1, 1, 2, 2,
          2, 2, 2, 2,
          1, 2, 2, 2,
          2, 2, 2, 1 ]

  # Compression of key from 56 bits to 48 bits
  key_comp = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32 ]

# Data tables for modified sbox
class modified_s_data:
  # Initial Permutation Table
  initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

  # Expansion D-box Table
  expansion_d_box = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
      6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
      12, 13, 12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25, 24, 25, 26, 27,
      28, 29, 28, 29, 30, 31, 32, 1 ]

  # Straight Permutation Table
  per = [ 16, 7, 20, 21,
      29, 12, 28, 17,
      1, 15, 23, 26,
      5, 18, 31, 10,
      2, 8, 24, 14,
      32, 27, 3, 9,
      19, 13, 30, 6,
      22, 11, 4, 25 ]

  # S-box Table
  s_box = [[
      [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ],
      [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]],
        
      [
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

      [ 
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
       [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
    
      [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
       [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
      
      [ [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
       [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
    
      [ 
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
       [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
      
      [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
      
      [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

  # Final Permutation Table
  final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25 ]

  # parity bit drop table
  keyp = [57, 49, 41, 33, 25, 17, 9,
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36,
      63, 55, 47, 39, 31, 23, 15,
      7, 62, 54, 46, 38, 30, 22,
      14, 6, 61, 53, 45, 37, 29,
      21, 13, 5, 28, 20, 12, 4 ]



  # Number of bit shifts
  shift_table = [1, 1, 2, 2,
          2, 2, 2, 2,
          1, 2, 2, 2,
          2, 2, 2, 1 ]

  # Compression of key from 56 bits to 48 bits
  key_comp = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32 ]

# data tables for modified permutation operation
class modified_p_data:
  # Initial Permutation Table
  initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

  # Expansion D-box Table
  expansion_d_box = [
      16, 17, 18, 19, 20, 21, 20, 21,
      6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
      12, 13, 12, 13, 14, 15, 16, 17,
      22, 23, 24, 25, 24, 25, 26, 27,
      32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
      28, 29, 28, 29, 30, 31, 32, 1 ]

  # Straight Permutation Table
  per = [ 
      2, 8, 24, 14,
      32, 27, 3, 9,
      5, 18, 31, 10,
      16, 7, 20, 21,
      29, 12, 28, 17,
      19, 13, 30, 6,
      1, 15, 23, 26,
      22, 11, 4, 25 ]

  # S-box Table
  s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
        
      [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

      [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
    
      [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
      
      [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
    
      [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
      
      [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
      
      [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

  # Final Permutation Table
  final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25 ]

  # parity bit drop table
  keyp = [57, 49, 41, 33, 25, 17, 9,
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36,
      63, 55, 47, 39, 31, 23, 15,
      7, 62, 54, 46, 38, 30, 22,
      14, 6, 61, 53, 45, 37, 29,
      21, 13, 5, 28, 20, 12, 4 ]



  # Number of bit shifts
  shift_table = [1, 1, 2, 2,
          2, 2, 2, 2,
          1, 2, 2, 2,
          2, 2, 2, 1 ]

  # Compression of key from 56 bits to 48 bits
  key_comp = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32 ]

# data tables for modified key data
class modified_key_data:
  # Initial Permutation Table
  initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

  # Expansion D-box Table
  expansion_d_box = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
      6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
      12, 13, 12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25, 24, 25, 26, 27,
      28, 29, 28, 29, 30, 31, 32, 1 ]

  # Straight Permutation Table
  per = [ 16, 7, 20, 21,
      29, 12, 28, 17,
      1, 15, 23, 26,
      5, 18, 31, 10,
      2, 8, 24, 14,
      32, 27, 3, 9,
      19, 13, 30, 6,
      22, 11, 4, 25 ]

  # S-box Table
  s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
        
      [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

      [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
    
      [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
      
      [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
    
      [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
      
      [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
      
      [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

  # Final Permutation Table
  final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25 ]

  # parity bit drop table
  keyp = [
      7, 62, 54, 46, 38, 30, 22,
      57, 49, 41, 33, 25, 17, 9,
      63, 55, 47, 39, 31, 23, 15,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36,
      1, 58, 50, 42, 34, 26, 18,
      14, 6, 61, 53, 45, 37, 29,
      21, 13, 5, 28, 20, 12, 4 ]



  # Number of bit shifts
  shift_table = [1, 1, 2, 2,
          2, 2, 2, 2,
          1, 2, 2, 2,
          2, 2, 2, 1 ]

  # Compression of key from 56 bits to 48 bits
  key_comp = [
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        46, 42, 50, 36, 29, 32, 
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        44, 49, 39, 56, 34, 53,
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10
        ]


# encryption function
def encrypt_64(pt, round_key_binary, round_key_hex):
    pt = d.hexadecimal_to_binary(pt)
    # Initial Permutation of plain text
    pt = d.permutation(pt, sd.initial_permutation, 64)
    print("After initial permutation", d.binary_to_hexadecimal(pt))
    # Splitting into plt and rpt
    left = pt[0:32]
    right = pt[32:64]
    for i in range(0, 16):
      print("For round",i+1)
      # Expanding the 32 bits data into 48 bits
      right_expanded = d.permutation(right, sd.expansion_d_box, 48)
      print("After round expansion:", d.binary_to_hexadecimal(right_expanded))
      # XOR RoundKey and right_expanded
      xor_x = d.xor(right_expanded, round_key_binary[i])
      print("After Xor of expanded RPT and round key:", d.binary_to_hexadecimal(xor_x))
      # substituting the value from s-box table by calculating row and column
      s_box_str = ""
      for j in range(0, 8):
        row = d.binary_to_decimal(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
        col = d.binary_to_decimal(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
        val = sd.s_box[j][row][col]
        s_box_str = s_box_str + d.decimal_to_binary(val)
      print("After S_box substitution:", d.binary_to_hexadecimal(s_box_str))
      # After substituting rearranging the bits
      s_box_str = d.permutation(s_box_str, sd.per, 32)
      print("After D-box permutation:", d.binary_to_hexadecimal(s_box_str))
      # XOR left and s_box_str
      result = d.xor(left, s_box_str)
      print("After Xor of left and right:", d.binary_to_hexadecimal(result))
      left = result
      # Swap lpt and rpt result
      if(i != 15):
        left, right = right, left
      print("Round ", i + 1, " LPT is ", d.binary_to_hexadecimal(left), " RPT is ", d.binary_to_hexadecimal(right), " Round key is ", round_key_hex[i],'\n')
    # Combination
    combine = left + right
    # final rearranging of bits to get cipher text
    cipher_text = d.permutation(combine, sd.final_perm, 64)
    return cipher_text

def DES_Key_generation(key):
  # Key generation
  # converting hex to binary
  key = d.hexadecimal_to_binary(key)
  #print("Initial Key:",key)
  # getting 56 bit key from 64 bit using the parity bits
  key = d.permutation(key, sd.keyp, 56)
  #print("Key after permutation:",key)
  # Splitting the key
  left = key[0:28] 
  right = key[28:56] 
  #print("Left key:",left,"\nRight Key",right)
  round_key_binary = [] # round_key_binary for RoundKeys in binary
  round_key_hex = [] # round_key_hex for RoundKeys in hexadecimal
  for i in range(0, 16):
    # Shifting the bits by nth shifts by checking from shift table
    left = d.shift_left(left, sd.shift_table[i])
    right = d.shift_left(right, sd.shift_table[i])
    #print("After shifting: left",left," right",right)
    # Combination of left and right string
    combine_str = left + right
    # Compression of key from 56 to 48 bits
    round_key = d.permutation(combine_str, sd.key_comp, 48)
    print("After Permutation into 48 bits for round",i+1,"Key is",d.binary_to_hexadecimal(round_key))
    round_key_binary.append(round_key)
    round_key_hex.append(d.binary_to_hexadecimal(round_key))
  return round_key_binary,round_key_hex

# defining the function for avalanche effect
def get_Avalanche_score(s1,s2):
  #print(len(s1))
  #print(s1)
  count = 0
  for j in range(len(s1)):
    if s1[j] != s2[j]:
      count = count + 1
  return count

# defining the function for doing the encryption and decryption
def algorithm(pt,key):
  print("Entered Plain Text is:",pt,'\n',"Entered Key is:",key,'\n')
  # generating keys
  round_key_binary,round_key_hex = DES_Key_generation(key)
  print("Encryption")
  cipher_text_s = d.binary_to_hexadecimal(encrypt_64(pt, round_key_binary, round_key_hex))
  print("Cipher Text : ",cipher_text_s,'\n')
  print("Decryption")
  round_key_binary_rev = round_key_binary[::-1]
  round_key_hex_rev = round_key_hex[::-1]
  text = d.binary_to_hexadecimal(encrypt_64(cipher_text_s, round_key_binary_rev, round_key_hex_rev))
  print("Plain Text : ",text)
  return cipher_text_s,text

d = simple_des()
sd = simple_data()

pt = input("Enter Plain Text (8 characters)\n").encode('utf-8').hex().upper()
key = input("Enter Key (8 characters)\n").encode('utf-8').hex().upper()


cipher_text_s,t = algorithm(pt,key)
print("Cipher text is:",cipher_text_s,'\n',"Plain text is:",t,'\n')

# creating menu/options for users.
cipher_text_m = []
plain_text = []
x = 'y'
while x == 'y':
  choice = input("Menu for Modification operation: \n 1. Substitution \n 2. Permutation \n 3. Xor \n 4. Block Size \n 5. Key \n Enter your choice \n")
  if choice == "1":
    sd = modified_s_data()
    t = 64
  elif choice == "2":
    sd = modified_p_data()
    t = 64
  elif choice == "3":
    d = modified_des_xor()
    t = 64
  elif choice == "4":
    t = int(input("Enter modified Block size(in bits)\n"))
    sd = simple_data()
  elif choice == "5":
    sd = modified_key_data()
    t = 64
  else:
    print("Wrong Choice...!!!!")
    break
  c,t = algorithm(pt[0:int(t/4)],key)
  cipher_text_m = c
  plain_text = t
  print("Cipher text is",cipher_text_m)
  print("Decrypted text is",plain_text)
  print("For avalanche effect:\n")
  a = get_Avalanche_score(cipher_text_s[2:],cipher_text_m[2:])
  print("No. of different characters:",a)
  print("Avalanche effect:",a/len(cipher_text_s[2:])*100,'%')
  x = input("\nDo you want to continue...y/n\n")


l = input("Do you want to view a demo of arbitary plain text encryption...y/n\n")
if l == "y":
  print("This is an example of data of arbitarary size.\n")
  s = input("Enter plaintext\n").encode('utf-8')
  print("Initial Plain text:",s)
  s1 = s.hex().upper()
  print("Plain text after padding if required:",s1)
  s2 =[]
  for i in range(len(s1)%16):
    s1+="0"
  x = ''
  for i in range(1,len(s1)+1):
    x+=s1[i-1]
    if i % 16 == 0:
      s2.append(x)
      x=''
  k = input("Enter key 8 characters\n").encode('utf-8').hex().upper()
  e = ""
  de = ""
  round_key_binary,round_key_hex = DES_Key_generation(k)
  print("Encryption")
  for i in range(len(s2)):
    cipher_text_st = d.binary_to_hexadecimal(encrypt_64(s2[i], round_key_binary, round_key_hex))
    print("Cipher Text : ",cipher_text_st,'\n')
    plain_text_st = d.binary_to_hexadecimal(encrypt_64(cipher_text_st[2:], round_key_binary[::-1], round_key_hex[::-1]))
    print("Decrypted Text : ",plain_text_st)
    e+=cipher_text_st
    de+=plain_text_st
  print("Complete cipher text is:",e)
  print("Complete decrypted text is:",de)
else:
  print("Thank you for your time...\n")
