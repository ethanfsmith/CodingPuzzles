#---------------------------------------SOLUTIONS------------------------------------------------
#--------------------------------------Warm UP---------------------------------------------------
#ABC's
def getSum(A: int, B: int, C: int) -> int:
  # Write your code here
  answer = A + B + C
  return answer

#All Wrong
def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  wrongAnswer = ''

  for answer in C:
    if answer == 'A':
        wrongAnswer += 'B'
    elif answer == 'B':
        wrongAnswer += 'A'

  return wrongAnswer

#BattleShip
from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  ships = 0

  for row in G:
    ships += sum(row)
      
  return ships /(R*C)

#--------------------------------------Level 1------------------------------------------------

#Cafeteria-------------------------------------------------------------------
from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  diners = 0

  # Sort the seats in ascending order
  S.sort()

  # Evaluate the first seat
  if S[0] > K:
      diners = (S[0] - 1) // (K + 1)

  # Evaluate middle seats
  prev = S[0]
  for seat in S[1:]:
      if (seat - prev) > K:
          diners += (seat - prev - K - 1) // (K + 1)
      prev = seat

  # Evaluate the last seat
  if N > S[-1] + K:
      diners += (N - S[-1]) // (K + 1)

  return diners

#Director of Photography----------------------------------------------------------------
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  artisticPhotographs = 0

  # Only search for artistic photographs
  for i in range(N - (2 * X)):
      if C[i] == 'P' or C[i] == 'B':
          for j in range(i + X, min(i + (Y + 1), N - X)):
              if C[j] == 'A':
                  for k in range(j + X, min(j + (Y + 1), N)):
                      if (C[k] == 'B' and C[i] == 'P') or (C[k] == 'P' and C[i] == 'B'):
                          # P or B from A
                          artisticPhotographs += 1

  return artisticPhotographs

#Kaitenzushi------------------------------------------------------------
from typing import List
# Write any import statements here
from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:

  eaten = 0  # count of dishes eaten
  kQ = deque()  # deque for dishes eaten in K range
  k_Set = set()  # set for sorted values of dishes eaten in K range

  # Loop through each incoming dish
  for inDish in D:
    if inDish not in k_Set:  # Quickly search sorted set for dish
        if len(kQ) == K:  # Manage deque and set for size K
            k_Set.remove(kQ.popleft())
        kQ.append(inDish)  # Add dish to K
        k_Set.add(inDish)  # Add dish to K
        eaten += 1  # Track dishes eaten

  return eaten

#Rotary Lock------------------------------------------------------------------
from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  time = 0                 # time to enter code
  current = 1             # starting position of the lock

  # Loop through each lock value
  for num in C:
      # Sum time choosing minimum direct or indirect rotation between numbers
      time += min(abs(current - num), abs((N - max(current, num)) + min(current, num)))
      current = num

  return time

#Scoreboard Inference-----------------------------------------------------------------
from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  even = 0
  odd = 0
  S.sort()

  # Find min even and odd in the list
  for score in S:
      odd = max(odd, score % 2)
      if score > even:
          even = score // 2

  return even + odd

#Stack Stabilization---------------------------------------------------------------------
from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:

  deflate = 0

  for disc in range(N - 2, -1, -1):  # Search stack from top to bottom
      if R[disc] >= R[disc + 1]:
          R[disc] = R[disc + 1] - 1  # Deflate disc to appropriate size
          deflate += 1
      if R[disc] <= 0:  # Impossible if 0 or less
          return -1

  return deflate

#Uniform Integers--------------------------------------------------------------------------
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  count = 0

  # Convert A and B to strings to get the length of the largest number
  max_length = max(len(str(A)), len(str(B)))

  # Iterate from 1 to the maximum length
  for length in range(1, max_length + 1):
      # Iterate through all possible digits from 0 to 9
      for digit in range(10):
          # Generate the uniform number with the current digit repeated for the current length
          uniform = int(str(digit) * length)
          # Check if the uniform number is within the range [A, B]
          if uniform >= A and uniform <= B:
              count += 1

  return count

#--------------------------------------Level 2------------------------------------------------

#Director of Photography--------------------------------------------------------------------------
import bisect

def getArtisticPhotographCount2(N: int, C: str, X: int, Y: int) -> int:
    artistic = 0
    Pi, Ai, Bi = [], [], [] # Lists to store the indexes for each character

    # Find all P, A, B locations
    for i in range(N):
        if C[i] == 'P':
            Pi.append(i)
        elif C[i] == 'A':
            Ai.append(i)
        elif C[i] == 'B':
            Bi.append(i)

    # Calculate combinations for each artistic photo
    # Combinations = count of P * count of B
    for location in Ai:

        # PAB
        pLower = bisect.bisect_left(Pi, location - Y)
        pUpper = bisect.bisect_right(Pi, location - X)
        bLower = bisect.bisect_left(Bi, location + X)
        bUpper = bisect.bisect_right(Bi, location + Y)
        artistic += (pUpper - pLower) * (bUpper - bLower)

        # BAP
        pLower = bisect.bisect_left(Pi, location + X)
        pUpper = bisect.bisect_right(Pi, location + Y)
        bLower = bisect.bisect_left(Bi, location - Y)
        bUpper = bisect.bisect_right(Bi, location - X)
        artistic += (pUpper - pLower) * (bUpper - bLower)

    return artistic

#Hops--------------------------------------------------------------------------
from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  lily = 0

  P.sort()

  # Count open lily pads between N and furthest frog
  lily += N - P[-1] - 1
  for i in range(len(P) - 1, 0, -1):
      lily += P[i] - P[i - 1] - 1

  return lily + F



#---------------------------------------Test Cases------------------------------------------------
#ABC's
print("ABC's")
print(getSum(1,2,3))
print()

#All Wrong
print("All Wrong")
print(getWrongAnswers(3,("ABA")))
print()

#Battleship
print("Battleship")

R = 2
C = 3
G = [[0, 0, 1],
     [1, 0, 1]]
print(getHitProbability(R, C, G))
print()

#Cafeteria
print("Cafeteria")

N = 10
K = 1
M = 2
S = [2,6]
print(getMaxAdditionalDinersCount(N,K,M,S))

N = 15
K = 2
M = 3
S = [11,6,14]
print(getMaxAdditionalDinersCount(N,K,M,S))
print()

#Director of Photography
print("Director of Photography")

N=5
C="APABA"
X=1
Y=1
print(getArtisticPhotographCount(N,C,X,Y))

N=5
C="APABA"
X=2
Y=3
print(getArtisticPhotographCount(N,C,X,Y))

N=8
C=".PBAAP.B"
X=1
Y=3
print(getArtisticPhotographCount(N,C,X,Y))
print()

#Kaitenzushi
print("Kaitenzushi")

N = 6
D = [1,2,3,3,2,1]
K=1
print(getMaximumEatenDishCount(N,D,K))

N = 6
D = [1,2,3,3,2,1]
K=2
print(getMaximumEatenDishCount(N,D,K))

N = 7
D = [1,2,1,2,1,2,1]
K=2
print(getMaximumEatenDishCount(N,D,K))
print()

#Rotary Lock
print("Rotary Lock")

N = 3
M = 3
C = [1,2,3]
print(getMinCodeEntryTime(N,M,C))

N = 10
M=  4
C = [9, 4, 4, 8]
print(getMinCodeEntryTime(N,M,C))
print()

#Scoreboard Inference
print("Scoreboard Inference")

N =6
S = [1, 2, 3, 4, 5, 6]
print(getMinProblemCount(N,S))

N =4
S = [4,3,3,4]
print(getMinProblemCount(N,S))

N = 4
S = [2, 4, 6, 8]
print(getMinProblemCount(N,S))
print()

#Stack Stabilization
print("Stack Stabilization")

N = 5
R = [2, 5, 3, 6, 5]
print(getMinimumDeflatedDiscCount(N,R))

N = 3
R = [100, 100, 100]
print(getMinimumDeflatedDiscCount(N,R))

N = 4
R = [6, 5, 4, 3]
print(getMinimumDeflatedDiscCount(N,R))
print()

#Uniform Integers
print("Uniform Integers")

A = 75
B = 300
print(getUniformIntegerCountInInterval(A,B))

A = 1
B = 9
print(getUniformIntegerCountInInterval(A,B))

A = 99999999999
B = 99999999999
print(getUniformIntegerCountInInterval(A,B))

#Director of Photography 2
print("Director of Photography 2")

N=5
C="APABA"
X=1
Y=1
print(getArtisticPhotographCount(N,C,X,Y))

N=5
C="APABA"
X=2
Y=3
print(getArtisticPhotographCount(N,C,X,Y))

N=8
C=".PBAAP.B"
X=1
Y=3
print(getArtisticPhotographCount(N,C,X,Y))
print()

#Hops
print("Hops")

N = 3
F = 1
P = [1]
print(getSecondsREquired(N,F,P))

N = 6
F = 3
P = [5, 2, 4]
print(getSecondsREquired(N,F,P))
print()