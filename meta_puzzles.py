#---------------------------------------SOLUTIONS------------------------------------------------
#--------------------------------------Warm UP
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

#--------------------------------------Level 1

#Cafeteria
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

#Director of Photography
import bisect

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
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
#--------------------------------------Level 2





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
