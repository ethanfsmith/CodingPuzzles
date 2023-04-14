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

#Director of Photography 2--------------------------------------------------------------------------
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

#Missing Mail--------------------------------------------------------------------

#Portals-------------------------------------------------------------------------

#Rabbit Hole 1-------------------------------------------------------------------
from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:

  webpages = 0                       # Start with 0 links visited
  pageCount = [0] * N                # Track count of links from index
  visited = set()                    # Track visited pages, utilize set for search

  for i in range(N):
      # Only evaluate new pages
      if pageCount[i] == 0:
          # Link within available pages
          link = L[i] - 1
          if link < N:
              # Enter the page
              pageCount[i] += 1

              # Evaluate the links
              while link < N and link not in visited and link != i:
                  # If the link has been evaluated, add the evaluation to the current count
                  if pageCount[link] > 0:
                      pageCount[i] += pageCount[link]
                      break
                  else:
                      pageCount[i] += 1       # Go to the new page
                      visited.add(link)       # Track visited pages
                      link = L[link] - 1      # Retrieve the link

          # Track max webpages
          webpages = max(webpages, pageCount[i])

          # Empty visited set
          while visited:
              # Circular reference loop, assign all values in loop to value
              if link == i:
                  pageCount[visited.pop()] = pageCount[i]
              else:
                  visited.pop()

  return webpages

#Rotary Lock 2--------------------------------------------------------------------
from typing import List
# Write any import statements here

def getMinCodeEntryTime2(N: int, M: int, C: List[int]) -> int:
  times = [0] * M  # list of times
  time = float('inf')  # time set to infinity

  for i in range(M):
      # time to value including starting position
      times[i] = times[0] + min(abs(1 - C[i]), abs((N - max(1, C[i])) + min(1, C[i])))

      for j in range(i):
          # compare with previous
          if j > 0:
              comp = times[j] + min(abs(C[j - 1] - C[i]), abs((N - max(C[j - 1], C[i])) + min(C[j - 1], C[i])))
              times[i] = min(times[i], comp)

          # previous time plus recent move
          times[j] = times[j] + min(abs(C[i - 1] - C[i]), abs((N - max(C[i - 1], C[i])) + min(C[i - 1], C[i])))

  # search for minimum time
  time = min(times)

  return time

#Scoreboard Inference 2------------------------------------------------------------
from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Constraints
  if 1 <= N <= 500000:
      p1, p2, p3 = 0, 0, 0
      one_present = 0
      odd = False

      S.sort()

      # Check if the number 1 is in the set
      if 1 in S:
          one_present = 1

      for score in S:
          # Determine if score set contains an odd number
          if score % 2 == 1:
              odd = True

          # Score - sum(problems) gives minimum additional problems
          p3 += (score - (p1 + p2 * 2 + p3 * 3)) // 3

          # Modulus gives additional min problem p1 or p2
          if (score - (p1 + p2 * 2 + p3 * 3)) % 3 == 1:
              p1 += 1
          elif (score - (p1 + p2 * 2 + p3 * 3)) % 3 == 2:
              p2 += 1

          # Verify 1's count
          if odd:
              if p1 > (one_present + 1):
                  p1 -= 2
                  p2 += 1
          else:
              if p1 > 3:
                  p1 -= 3
                  p3 += 1

          # Verify 2's count
          if p2 > 4 or (p1 > 0 and p2 > 3 and one_present == 0):
              p2 -= 3
              p3 += 2

          # Manage 3's count
          if one_present == 1:
              if p1 > 1 and p2 > 1:
                  p1 -= 1
                  p2 -= 1
                  p3 += 1
          else:
              if p1 > 0 and p2 > 2:
                  p1 -= 1
                  p2 -= 1
                  p3 += 2

      return p1 + p2 + p3

#Tunnel Time------------------------------------------------------------
from typing import List
# Write any import statements here

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  seconds = 0
  tunnel_length = 0
  partial_tunnel = 0
  A.sort()
  B.sort()

  # Find total tunnel length
  for i in range(N):
      tunnel_length += B[i] - A[i]

  # Tunnels end on a tunnel exit
  if K % tunnel_length == 0:
      seconds = B[N - 1]
      seconds += ((K // tunnel_length) - 1) * C
  else:
      # Total complete laps in tunnel length
      seconds += (K // tunnel_length) * C

      # Remaining distance from tunnel length
      for i in range(N):
          if K % tunnel_length <= (partial_tunnel + (B[i] - A[i])):
              seconds += A[i] + (K % tunnel_length - partial_tunnel)
              break
          partial_tunnel += B[i] - A[i]

  return seconds

#--------------------------------------Level 3------------------------------------------------

#Boss Fight------------------------------------------------------------
from typing import List
# Write any import statements here

def get_damage(w1, w2, B):
  # Function to calculate damage dealt by two warriors to the boss
  return (w1[0] / B) * w1[1] + (w1[0] / B) * w2[1] + (w2[0] / B) * w2[1]

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  warrior = []
  w1 = [H[0], D[0]]
  w2 = [H[1], D[1]]
  damage12 = get_damage(w1, w2, B)
  damage21 = get_damage(w2, w1, B)

  damage = max(damage12, damage21)  # Starting damage
  if damage21 > damage12:
      w1, w2 = w2, w1

  # Evaluate each remaining warrior
  for i in range(2, N):
      w3 = [H[i], D[i]]  # Assign new health and damage to w3

      # Compare damage for the third warrior to the 1st and 2nd warrior combinations
      damage13 = get_damage(w1, w3, B)
      damage32 = get_damage(w3, w2, B)
      damage31 = get_damage(w3, w1, B)
      damage23 = get_damage(w2, w3, B)

      # If any condition results in greater damage
      if max(damage13, max(damage32, max(damage31, damage23))) > damage:

          # Compare each combination for the greatest damage and adjust lineup
          # w1 w3
          if damage13 > max(damage32, max(damage31, damage23)):
              damage = damage13
              w2 = w3
          # w3 w2
          elif damage32 > max(damage13, max(damage31, damage23)):
              damage = damage32
              w1 = w3
          # w3 w1
          elif damage31 > max(damage13, max(damage32, damage23)):
              damage = damage31
              w2, w1 = w1, w3
          # w2 w3
          elif damage23 > max(damage13, max(damage32, damage31)):
              damage = damage23
              w1, w2 = w2, w3
          # Equal outcome, w1 == w2
          else:
              w1 = w3
      # Warriors within 1% of max damage
      elif 1 - max(damage32, max(damage31, damage23)) / damage <= 0.01:
          warrior.append(w3)

  # Evaluate contenders
  for W in warrior:
      damage = max(damage, max(get_damage(W, w2, B), get_damage(w1, W, B)))
      damage = max(damage, max(get_damage(w2, W, B), get_damage(W, w1, B)))

  return damage

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
print()

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
print(getSecondsRequired(N,F,P))

N = 6
F = 3
P = [5, 2, 4]
print(getSecondsRequired(N,F,P))
print()

#Missing Mail
print("Mising Mail")

print()

#Portals
print("Portals")

print()

#Rabbit Hole 1
print("Rabbit Hole 1")

N = 4
L =[4, 1, 2, 1]
print(getMaxVisitableWebpages(N,L))

N = 5
L =[4, 3, 5, 1, 2]
print(getMaxVisitableWebpages(N,L))

N = 5
L =[42, 4, 2, 2, 3]
print(getMaxVisitableWebpages(N,L))
print()

#Rotary Lock 2
print("Rotary Lock 2")

N = 3
M = 3
C = [1,2,3]
print(getMinCodeEntryTime2(N,M,C))

N = 10
M=  4
C = [9, 4, 4, 8]
print(getMinCodeEntryTime2(N,M,C))
print()

#Scoreboard Inference 2
print("Scoreboard Inference 2")

N = 5
S = [1, 2, 3, 4, 5]
print(getMinProblemCount(N,S))

N = 4
S = [4, 3, 3, 4]
print(getMinProblemCount(N,S))

N = 4
S = [2, 4, 6, 8]
print(getMinProblemCount(N,S))

N = 1
S = [8]
print(getMinProblemCount(N,S))
print()

#Tunnel Time
print("Tunnel Time")

C = 10
N = 2
A = [1, 6]
B = [3, 7]
K = 7
print(getSecondsElapsed(C,N,A,B,K))

C = 50
N = 3
A = [39, 19, 28]
B = [49, 27, 35]
K = 15
print(getSecondsElapsed(C,N,A,B,K))
print()

#Boss Fight
print("Boss Fight")

N =  3
H = [2, 1, 4]
D = [3, 1, 2]
B = 4
print(getMaxDamageDealt(N,H,D,B))

N =  4
H = [1, 1, 2, 100]
D = [1, 2, 1, 3]
B = 8
print(getMaxDamageDealt(N,H,D,B))

N =  4
H = [1, 1, 2, 3]
D = [1, 2, 1, 100]
B = 8
print(getMaxDamageDealt(N,H,D,B))
print()
