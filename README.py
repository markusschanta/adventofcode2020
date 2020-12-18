# ---
# jupyter:
#   jupytext:
#     hide_notebook_metadata: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Advent of Code 2020
#
# ## Table of Contents
#
# * [Day 1: Report Repair](#day-1-report-repair)
# * [Day 2: Password Philosophy](#day-2-password-philosophy)
# * [Day 3: Toboggan Trajectory](#day-3-toboggan-trajectory)
# * [Day 4: Passport Processing](#day-4-passport-processing)
# * [Day 5: Binary Boarding](#day-5-binary-boarding)
# * [Day 15: Rambunctious Recitation](#day-15-rambunctious-recitation)
# * [Day 16: Ticket Translation](#day-16-ticket-translation)
# * [Day 17: Conway Cubes](#day-17-conway-cubes)

# %% [markdown]
# ## Day 1: Report Repair
#
# After saving Christmas [five years in a row](https://adventofcode.com/events), you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
#
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them **stars**. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
#
# To save your vacation, you need to get all **fifty stars** by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!
#
# Before you leave, the Elves in accounting just need you to fix your **expense report** (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to **find the two entries that sum to** `2020` and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
#     1721
#     979
#     366
#     299
#     675
#     1456
#
# In this list, the two entries that sum to `2020` are `1721` and `299`. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is `514579`.
#
# Of course, your expense report is much larger. **Find the two entries that sum to `2020`; what do you get if you multiply them together?**
#
# Your puzzle answer was `224436`.

# %%
input = [1721, 979, 366, 299, 675, 1456]

# %%
input = open('input.1.txt', 'r').readlines()
input = [int(x) for x in input]

# %%
for i in input:
    j = 2020 - i
    if j in input:
        print("%d * %d = %d" % (i, j, i * j))

# %% [markdown]
# ### Part Two
#
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find **three** numbers in your expense report that meet the same criteria.
#
# Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`. Multiplying them together produces the answer, **`241861950`.**
#
# In your expense report, **what is the product of the three entries that sum to `2020`?**
#
# Your puzzle answer was `303394260`.

# %%
for i in input:
    for j in input:
        k = 2020 - i - j
        if k in input:
            print("%d * %d * %d = %d" % (i, j, k, i * j * k))

# %% [markdown]
# ## Day 2: Password Philosophy
#
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via [toboggan](https://en.wikipedia.org/wiki/Toboggan).
#
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.
#
# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input) of **passwords** (according to the corrupted database) and the **corporate policy when that password was set**.
#
# For example, suppose you have the following list:
#
#     1-3 a: abcde
#     1-3 b: cdefg
#     2-9 c: ccccccccc
#
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, `1-3 a` means that the password must contain `a` at least `1` time and at most `3` times.
#
# In the above example, `2` passwords are valid. The middle password, `cdefg`, is not; it contains no instances of `b`, but needs at least `1`. The first and third passwords are valid: they contain one `a` or nine `c`, both within the limits of their respective policies.
#
# **How many passwords are valid** according to their policies?
#
# Your puzzle answer was `556`.

# %%
input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

# %%
input = open('input.2.txt', 'r').readlines()
input = [i.strip() for i in input]

# %%
import numpy as np
import re

REGEX = re.compile("(.*)-(.*) (.*): (.*)")

def valid(input_line):
    p_min, p_max, p, s = REGEX.match(input_line).groups()
    return int(p_min) <= s.count(p) <= int(p_max)

np.sum([valid(i) for i in input])


# %% [markdown]
# ### Part Two
#
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.
#
# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
#
# Each policy actually describes two **positions in the password**, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) **Exactly one of these positions** must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
# Given the same example list from above:
#
# * `1-3 a: abcde` is **valid**: position `1` contains `a` and position `3` does not.
# * `1-3 b: cdefg` is **invalid**: neither position `1` nor position `3` contains `b`.
# * `2-9 c: ccccccccc` is **invalid**: both position `2` and position `9` contain `c`.
#
# **How many passwords are valid** according to the new interpretation of the policies?
#
# Your puzzle answer was `605`.

# %%
def valid2(input_line):
    i, j, p, s = REGEX.match(input_line).groups()
    return (s[int(i) - 1] == p) != (s[int(j) - 1] == p)

np.sum([valid2(i) for i in input])

# %% [markdown]
# ## Day 3: Toboggan Trajectory
#
# With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.
#
# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (`.`) and trees (`#`) you can see. For example:
#
#     ..##.......
#     #...#...#..
#     .#....#..#.
#     ..#.#...#.#
#     .#...##..#.
#     ..#.##.....
#     .#.#.#....#
#     .#........#
#     #.##...#...
#     #...##....#
#     .#..#...#.#
#
# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
#
#     ..##.........##.........##.........##.........##.........##.......  --->
#     #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#     .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#     ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#     .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#     ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
#     .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#     .#........#.#........#.#........#.#........#.#........#.#........#
#     #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#     #...##....##...##....##...##....##...##....##...##....##...##....#
#     .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# You start on the open square (`.`) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
#
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by **counting all the trees** you would encounter for the slope **right 3, down 1**:
#
# From your starting position at the top-left, check the position that is right `3` and down `1`. Then, check the position that is right `3` and down `1` from there, and so on until you go past the bottom of the map.
#
# The locations you'd check in the above example are marked here with `O` where there was an open square and `X` where there was a tree:
#
#     ..##.........##.........##.........##.........##.........##.......  --->
#     #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#     .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#     ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#     .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#     ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
#     .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#     .#........#.#........X.#........#.#........#.#........#.#........#
#     #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#     #...##....##...##....##...#X....##...##....##...##....##...##....#
#     .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# In this example, traversing the map using this slope would cause you to encounter `7` trees.
#
# Starting at the top-left corner of your map and following a slope of right `3` and down `1`, **how many trees would you encounter?**

# %%
input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

# %%
input = open('input.3.txt', 'r').readlines()
input = [i.strip() for i in input]


# %%
def is_tree(x, y):
    line = input[y]
    return line[x % len(line)] == '#'

trees = 0

for i in range(len(input)):
    if is_tree(3 * i, i):
        trees += 1

trees


# %% [markdown]
# ### Part Two
#
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
#
# * Right 1, down 1.
# * Right 3, down 1. (This is the slope you already checked.)
# * Right 5, down 1.
# * Right 7, down 1.
# * Right 1, down 2.
#
# In the above example, these slopes would find `2`, `7`, `3`, `4`, and `2` tree(s) respectively; multiplied together, these produce the answer **`336`**.
#
# **What do you get if you multiply together the number of trees encountered on each of the listed slopes?**
#
# Your puzzle answer was `2122848000`.

# %%
def num_trees(v_x, v_y):
    x = 0
    y = 0
    trees = 0
    while y < len(input):
        trees += is_tree(x, y)
        x += v_x
        y += v_y
    return trees

num_trees(3, 1)

# %%
speeds = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

np.prod([num_trees(*s) for s in speeds])

# %% [markdown]
# ## Day 4: Passport Processing
#
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.
#
# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.
#
# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.
#
# The automatic passport scanners are slow because they're having trouble **detecting which passports have all required fields**. The expected fields are as follows:
#
# * `byr` (Birth Year)
# * `iyr` (Issue Year)
# * `eyr` (Expiration Year)
# * `hgt` (Height)
# * `hcl` (Hair Color)
# * `ecl` (Eye Color)
# * `pid` (Passport ID)
# * `cid` (Country ID)
#
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of `key:value` pairs separated by spaces or newlines. Passports are separated by blank lines.
#
# Here is an example batch file containing four passports:
#
#     ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
#     byr:1937 iyr:2017 cid:147 hgt:183cm
#
#     iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
#     hcl:#cfa07d byr:1929
#
#     hcl:#ae17e1 iyr:2013
#     eyr:2024
#     ecl:brn pid:760753108 byr:1931
#     hgt:179cm
#
#     hcl:#cfa07d eyr:2025 pid:166559648
#     iyr:2011 ecl:brn hgt:59in
#
# The first passport is **valid** - all eight fields are present. The second passport is **invalid** - it is missing `hgt` (the Height field).
#
# The third passport is interesting; the **only missing field** is `cid`, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing `cid` fields. Treat this "passport" as **valid**.
#
# The fourth passport is missing two fields, `cid` and `byr`. Missing `cid` is fine, but missing any other field is not, so this passport is **invalid**.
#
# According to the above rules, your improved system would report **`2`** valid passports.
#
# Count the number of **valid** passports - those that have all required fields. Treat `cid` as optional. **In your batch file, how many passports are valid?**
#
# Your puzzle answer was `219`.

# %%
input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

# %%
input = open('input.4.txt', 'r').read()

# %%
passports = [{kv.split(":")[0]: kv.split(":")[1] for kv in p.split()} for p in input.split("\n\n")]

required = ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']

len([p for p in passports if set(p.keys()).issuperset(required)])

# %% [markdown]
# ### Part Two
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!
#
# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
#
# * `byr` (Birth Year) - four digits; at least `1920` and at most `2002`.
# * `iyr` (Issue Year) - four digits; at least `2010` and at most `2020`.
# * `eyr` (Expiration Year) - four digits; at least `2020` and at most `2030`.
# * `hgt` (Height) - a number followed by either `cm` or `in`:
#     * If cm, the number must be at least `150` and at most `193`.
#     * If in, the number must be at least `59` and at most `76`.
# * `hcl` (Hair Color) - a `#` followed by exactly six characters `0`-`9` or `a`-`f`.
# * `ecl` (Eye Color) - exactly one of: `amb` `blu` `brn` `gry` `grn` `hzl` `oth`.
# * `pid` (Passport ID) - a nine-digit number, including leading zeroes.
# * `cid` (Country ID) - ignored, missing or not.
#
# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:
#
#     byr valid:   2002
#     byr invalid: 2003
#
#     hgt valid:   60in
#     hgt valid:   190cm
#     hgt invalid: 190in
#     hgt invalid: 190
#
#     hcl valid:   #123abc
#     hcl invalid: #123abz
#     hcl invalid: 123abc
#
#     ecl valid:   brn
#     ecl invalid: wat
#
#     pid valid:   000000001
#     pid invalid: 0123456789
#
# Here are some invalid passports:
#
#     eyr:1972 cid:100
#     hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
#     iyr:2019
#     hcl:#602927 eyr:1967 hgt:170cm
#     ecl:grn pid:012533040 byr:1946
#
#     hcl:dab227 iyr:2012
#     ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
#     hgt:59cm ecl:zzz
#     eyr:2038 hcl:74454a iyr:2023
#     pid:3556412378 byr:2007
#
# Here are some valid passports:
#
#     pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
#     hcl:#623a2f
#
#     eyr:2029 ecl:blu cid:129 byr:1989
#     iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
#     hcl:#888785
#     hgt:164cm byr:2001 iyr:2015 cid:88
#     pid:545766238 ecl:hzl
#     eyr:2022
#
#     iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
#
# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
#
# Your puzzle answer was `127`.

# %%
input = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

# %%
input = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

# %%
input = open('input.4.txt', 'r').read()


# %%
def valid(passport):
    if "byr" not in passport: return False
    if not passport["byr"].isnumeric(): return False
    if not 1920 <= int(passport["byr"]) <= 2002: return False

    if "iyr" not in passport: return False
    if not passport["iyr"].isnumeric(): return False
    if not 2010 <= int(passport["iyr"]) <= 2020: return False

    if "eyr" not in passport: return False
    if not passport["eyr"].isnumeric(): return False
    if not 2020 <= int(passport["eyr"]) <= 2030: return False

    if "hgt" not in passport: return False
    if passport["hgt"][-2:] == 'cm':
        if not 150 <= int(passport["hgt"][:-2]) <= 193: return False
    elif passport["hgt"][-2:] == 'in':
        if not 59 <= int(passport["hgt"][:-2]) <= 76: return False
    else:
        return False

    if "hcl" not in passport: return False
    if not re.search(r'^#(?:[0-9a-f]{3}){1,2}$', passport["hcl"]): return False

    if "ecl" not in passport: return False
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False

    if "pid" not in passport: return False
    if not re.search(r'^\d{9}$', passport["pid"]): return False

    return True

passports = [{kv.split(":")[0]: kv.split(":")[1] for kv in p.split()} for p in input.split("\n\n")]
np.sum([valid(p) for p in passports])

# %% [markdown]
# ## Day 5: Binary Boarding
#
# You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.
#
# You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.
#
# Instead of [zones or groups](https://www.youtube.com/watch?v=oAHbLRjF0vo), this airline uses **binary space partitioning** to seat people. A seat might be specified like `FBFBBFFRLR`, where `F` means "front", `B` means "back", `L` means "left", and `R` means "right".
#
# The first 7 characters will either be `F` or `B`; these specify exactly one of the **128 rows** on the plane (numbered `0` through `127`). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the **front** (`0` through `63`) or the **back** (`64` through `127`). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
#
# For example, consider just the first seven characters of `FBFBBFFRLR`:
#
# * Start by considering the whole range, rows `0` through `127`.
# * `F` means to take the **lower half**, keeping rows `0` through `63`.
# * `B` means to take the **upper half**, keeping rows `32` through `63`.
# * `F` means to take the **lower half**, keeping rows `32` through `47`.
# * `B` means to take the **upper half**, keeping rows `40` through `47`.
# * `B` keeps rows `44` through `47`.
# * `F` keeps rows `44` through `45`.
# * The final `F` keeps the lower of the two, **row `44`**.
#
# The last three characters will be either `L` or `R`; these specify exactly one of the **8 columns** of seats on the plane (numbered `0` through `7`). The same process as above proceeds again, this time with only three steps. `L` means to keep the **lower half**, while `R` means to keep the **upper half**.
#
# For example, consider just the last 3 characters of `FBFBBFFRLR`:
#
# * Start by considering the whole range, columns `0` through `7`.
# * `R` means to take the **upper half**, keeping columns `4` through `7`.
# * `L` means to take the **lower half**, keeping columns `4` through `5`.
# * The final `R` keeps the upper of the two, column `5`.
#
# So, decoding `FBFBBFFRLR` reveals that it is the seat at **row `44`, column `5`**.
#
# Every seat also has a unique **seat ID**: multiply the row by 8, then add the column. In this example, the seat has ID `44 * 8 + 5 = 357`.
#
# Here are some other boarding passes:
#
# * BFFFBBFRRR: row `70`, column `7`, seat ID `567`.
# * FFFBBBFRRR: row `14`, column `7`, seat ID `119`.
# * BBFFBBFRLL: row `102`, column `4`, seat ID `820`.
#
# As a sanity check, look through your list of boarding passes. **What is the highest seat ID on a boarding pass?**
#
# Your puzzle answer was `864`.

# %%
input = 'BFFFBBFRRR'

# %%
input = 'FFFBBBFRRR'

# %%
input = 'BBFFBBFRLL'

# %%
input = open('input.5.txt', 'r').read().split('\n')


# %%
def seat_id(code):
    binary = code.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    return int(binary, 2)

seats = [seat_id(c) for c in input]

max(seats)

# %% [markdown]
# ### Part Two
#
# **Ding!** The "fasten seat belt" signs have turned on. Time to find your seat.
#
# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
#
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
#
# **What is the ID of your seat?**
#
# Your puzzle answer was `739`.

# %%
[i for i in range(min(seats), max(seats)) if i not in seats][0]

# %% [markdown]
# ## Day 15: Rambunctious Recitation
#
# You catch the airport shuttle and try to book a new flight to your vacation island. Due to the storm, all direct flights have been cancelled, but a route is available to get around the storm. You take it.
#
# While you wait for your flight, you decide to check in with the Elves back at the North Pole. They're playing a **memory game** and are ever so excited to explain the rules!
#
# In this game, the players take turns saying **numbers**. They begin by taking turns reading from a list of **starting numbers** (your puzzle input). Then, each turn consists of considering the **most recently spoken number**:
#
# * If that was the **first** time the number has been spoken, the current player says `0`.
# * Otherwise, the number had been spoken before; the current player announces **how many turns apart** the number is from when it was previously spoken.
#
# So, after the starting numbers, each turn results in that player speaking aloud either `0` (if the last number is new) or an **age** (if the last number is a repeat).
#
# For example, suppose the starting numbers are `0, 3, 6`:
#
# * **Turn 1**: The `1`st number spoken is a starting number, **`0`**.
# * **Turn 2**: The `2`nd number spoken is a starting number, **`3`**.
# * **Turn 3**: The `3`rd number spoken is a starting number, **`6`**.
# * **Turn 4**: Now, consider the last number spoken, `6`. Since that was the first time the number had been spoken, the `4`th number spoken is **`0`**.
# * **Turn 5**: Next, again consider the last number spoken, `0`. Since it had been spoken before, the next number to speak is the difference between the turn number when it was last spoken (the previous turn, `4`) and the turn number of the time it was most recently spoken before then (turn `1`). Thus, the 5th number spoken is `4 - 1`, **`3`**.
# * **Turn 6**: The last number spoken, `3` had also been spoken before, most recently on turns `5` and `2`. So, the `6`th number spoken is `5 - 2`, **`3`**.
# * **Turn 7**: Since `3` was just spoken twice in a row, and the last two turns are `1` turn apart, the `7`th number spoken is **`1`**.
# * **Turn 8**: Since `1` is new, the `8`th number spoken is **`0`**.
# * **Turn 9**: `0` was last spoken on turns `8` and `4`, so the `9`th number spoken is the difference between them, **`4`**.
# * **Turn 10**: `4` is new, so the `10`th number spoken is **`0`**.
#
# (The game ends when the Elves get sick of playing or dinner is ready, whichever comes first.)
#
# Their question for you is: what will be the **`2020`th** number spoken? In the example above, the `2020`th number spoken will be `436`.
#
# Here are a few more examples:
#
# * Given the starting numbers `1,3,2`, the `2020`th number spoken is `1`.
# * Given the starting numbers `2,1,3`, the `2020`th number spoken is `10`.
# * Given the starting numbers `1,2,3`, the `2020`th number spoken is `27`.
# * Given the starting numbers `2,3,1`, the `2020`th number spoken is `78`.
# * Given the starting numbers `3,2,1`, the `2020`th number spoken is `438`.
# * Given the starting numbers `3,1,2`, the `2020`th number spoken is `1836`.
#
# Given your starting numbers, **what will be the `2020`th number spoken?**
#
# Your puzzle input is `1,12,0,20,8,16`.

# %%
input = [0, 3, 6]

# %%
input = [1, 3, 2]

# %%
input = [2, 1, 3]

# %%
input = [1, 12, 0, 20, 8, 16]

# %%
n = 2020

sequence = []

for i in range(1, n + 1):
    if i <= len(input):
        sequence.append(input[i - 1])
    else:
        last = sequence[-1]
        occurrences = [i for i, n in enumerate(sequence[::-1]) if n == last]
        assert len(occurrences) > 0
        if len(occurrences) == 1:
            sequence.append(0)
        elif len(occurrences) >= 2:
            sequence.append(occurrences[1] - occurrences[0])

sequence[n - 1]

# %% [markdown]
# ## Part Two
#
# Impressed, the Elves issue you a challenge: determine the `30000000`th number spoken. For example, given the same starting numbers as above:
#
# * Given `0,3,6`, the `30000000`th number spoken is `175594`.
# * Given `1,3,2`, the `30000000`th number spoken is `2578`.
# * Given `2,1,3`, the `30000000`th number spoken is `3544142`.
# * Given `1,2,3`, the `30000000`th number spoken is `261214`.
# * Given `2,3,1`, the `30000000`th number spoken is `6895259`.
# * Given `3,2,1`, the `30000000`th number spoken is `18`.
# * Given `3,1,2`, the `30000000`th number spoken is `362`.
#
# Given your starting numbers, **what will be the `30000000`th number spoken?**
#
# Your puzzle answer was `47205`.

# %%
n = 2020

sequence = []

for i in range(1, n + 1):
    if i <= len(input):
        sequence.insert(0, input[i - 1])
    else:
        last = sequence[0]
        try:
            previous = sequence.index(last, 1)
            sequence.insert(0, previous)
        except ValueError:
            sequence.insert(0, 0)

sequence[0]

# %%
n = 2020

mentions = {}

for i in range(1, n + 1):
    if i <= len(input):
        mentions[input[i - 1]] = [i]
        last = input[i - 1]
    else:
        if len(mentions[last]) == 1:
            age = 0
        else:
            age = mentions[last][0] - mentions[last][1]
        last = age
        if age in mentions:
            mentions[age] = [i, mentions[age][0]]
        else:
            mentions[age] = [i]

last

# %% [markdown]
# ## Day 16: Ticket Translation
#
# As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.
#
# Unfortunately, you can't actually **read** the words on the ticket. You can, however, read the numbers, and so you figure out **the fields these tickets must have** and **the valid ranges** for values in those fields.
#
# You collect the **rules for ticket fields**, the **numbers on your ticket**, and the **numbers on other nearby tickets** for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).
#
# The **rules for ticket fields** specify a list of fields that exist **somewhere** on the ticket and the **valid ranges of values** for each field. For example, a rule like `class: 1-3 or 5-7` means that one of the fields in every ticket is named `class` and can be any value in the ranges `1-3` or `5-7` (inclusive, such that `3` and `5` are both valid in this field, but `4` is not).
#
# Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:
#
#     .--------------------------------------------------------.
#     | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
#     |                                                        |
#     | ??: 301  ??: 302             ???????: 303      ??????? |
#     | ??: 401  ??: 402           ???? ????: 403    ????????? |
#     '--------------------------------------------------------'
#
# Here, `?` represents text in a language you don't understand. This ticket might be represented as `101,102,103,104,301,302,303,401,402,403`; of course, the actual train tickets you're looking at are **much** more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!
#
# Start by determining which tickets are **completely invalid**; these are tickets that contain values which **aren't valid for any field**. Ignore **your ticket** for now.
#
# For example, suppose you have the following notes:
#
#     class: 1-3 or 5-7
#     row: 6-11 or 33-44
#     seat: 13-40 or 45-50
#
#     your ticket:
#     7,1,14
#
#     nearby tickets:
#     7,3,47
#     40,4,50
#     55,2,20
#     38,6,12
#
# It doesn't matter which position corresponds to which field; you can identify invalid **nearby tickets** by considering only whether tickets contain **values that are not valid for any field**. In this example, the values on the first **nearby ticket** are all valid for at least one field. This is not true of the other three **nearby tickets**: the values `4`, `55`, and `12` are are not valid for any field. Adding together all of the invalid values produces your **ticket scanning error rate**: `4 + 55 + 12 = 71`.
#
# Consider the validity of the **nearby tickets** you scanned. **What is your ticket scanning error rate?**
#
# Your puzzle answer was `27911`.

# %%
input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

# %%
input = open('input.16.txt', 'r').read()

# %%
import re

def parse_fields(s):
    parts = REGEX.match(s).groups()
    assert len(parts) == 5
    return parts[0], [[int(parts[1]), int(parts[2])], [int(parts[3]), int(parts[4])]]

def is_in_fields(number):
    for f in fields:
        v = list(f.values())[0]
        if v[0][0] <= number <= v[0][1]: return True
        if v[1][0] <= number <= v[1][1]: return True
    return False

REGEX = re.compile("(.*): (.*)-(.*) or (.*)-(.*)")

fields, ticket, tickets = input.split("\n\n")
fields = fields.split("\n")
fields = [{k: v} for f in fields for k, v in [parse_fields(f)]]

ticket = [int(s) for s in ticket.split("\n")[1].split(",")]

tickets = [[int(s) for s in t.split(",")] for t in tickets.split("\n")[1:]]
tickets = np.array(tickets)

not_in_fields = set([n for n in np.arange(tickets.min(), tickets.max() + 1) if not is_in_fields(n)])

np.sum([n for n in tickets.flat if n in not_in_fields])

# %% [markdown]
# ### Part Two
#
# Now that you've identified which tickets contain invalid values, **discard those tickets entirely**. Use the remaining valid tickets to determine which field is which.
#
# Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if `seat` is the third field, it is the third field on every ticket, including **your ticket**.
#
# For example, suppose you have the following notes:
#
#     class: 0-1 or 4-19
#     row: 0-5 or 8-19
#     seat: 0-13 or 16-19
#
#     your ticket:
#     11,12,13
#
#     nearby tickets:
#     3,9,18
#     15,1,5
#     5,14,9
#
# Based on the **nearby tickets** in the above example, the first position must be `row`, the second position must be `class`, and the third position must be `seat`; you can conclude that in **your ticket**, `class` is `12`, `row` is `11`, and `seat` is `13`.
#
# Once you work out which field is which, look for the six fields on **your ticket** that start with the word `departure`. **What do you get if you multiply those six values together?**
#
# Your puzzle answer was `737176602479`.

# %%
import pandas as pd

def possible_fields(number):
    possible = []
    for f in fields:
        k = list(f.keys())[0]
        v = list(f.values())[0]
        if v[0][0] <= number <= v[0][1]:
            possible += [k]
        if v[1][0] <= number <= v[1][1]:
            possible += [k]
    return possible

df = pd.DataFrame(tickets)

p = df.applymap(lambda t: set(possible_fields(t)))
p = p.loc[p.applymap(lambda l: len(l)).min(axis=1).gt(0), :]

cc = [set.intersection(*c) for _, c in p.iteritems()]

known = [None] * len(cc)
lcc = [len(c) for c in cc]
while max(lcc) > 0:
    i = lcc.index(1)
    f = list(cc[i])[0]
    known[i] = f
    cc = [c - {f} for c in cc]
    lcc = [len(c) for c in cc]

np.prod([ticket[i] for i, k in enumerate(known) if k.startswith('departure')])

# %% [markdown]
# ## Day 17: Conway Cubes
#
# As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.
#
# The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.
#
# The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (`x`,`y`,`z`), there exists a single cube which is either **active** or **inactive**.
#
# In the initial state of the pocket dimension, almost all cubes start **inactive**. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified **active** (`#`) or **inactive** (`.`) state.
#
# The energy source then proceeds to boot up by executing six **cycles**.
#
# Each cube only ever considers its **neighbors**: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at `x=1,y=2,z=3`, its neighbors include the cube at `x=2,y=2,z=2`, the cube at `x=0,y=2,z=3`, and so on.
#
# During a cycle, all cubes simultaneously change their state according to the following rules:
#
# * If a cube is **active** and **exactly `2` or `3`** of its neighbors are also active, the cube remains **active**. Otherwise, the cube becomes **inactive**.
# * If a cube is **inactive** but **exactly `3`** of its neighbors are active, the cube becomes **active**. Otherwise, the cube remains **inactive**.
#
# The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.
#
# For example, consider the following initial state:
#
#     .#.
#     ..#
#     ###
#
# Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given `z` coordinate (and the frame of view follows the active cells in each cycle):
#
# Before any cycles:
#
#     z=0
#     .#.
#     ..#
#     ###
#
#
# After 1 cycle:
#
#     z=-1
#     #..
#     ..#
#     .#.
#
#     z=0
#     #.#
#     .##
#     .#.
#
#     z=1
#     #..
#     ..#
#     .#.
#
# After 2 cycles:
#
#     z=-2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-1
#     ..#..
#     .#..#
#     ....#
#     .#...
#     .....
#
#     z=0
#     ##...
#     ##...
#     #....
#     ....#
#     .###.
#
#     z=1
#     ..#..
#     .#..#
#     ....#
#     .#...
#     .....
#
#     z=2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
# After 3 cycles:
#
#     z=-2
#     .......
#     .......
#     ..##...
#     ..###..
#     .......
#     .......
#     .......
#
#     z=-1
#     ..#....
#     ...#...
#     #......
#     .....##
#     .#...#.
#     ..#.#..
#     ...#...
#
#     z=0
#     ...#...
#     .......
#     #......
#     .......
#     .....##
#     .##.#..
#     ...#...
#
#     z=1
#     ..#....
#     ...#...
#     #......
#     .....##
#     .#...#.
#     ..#.#..
#     ...#...
#
#     z=2
#     .......
#     .......
#     ..##...
#     ..###..
#     .......
#     .......
#     .......
#
# After the full six-cycle boot process completes, `112` cubes are left in the **active** state.
#
# Starting with your given initial configuration, simulate six cycles. **How many cubes are left in the active state after the sixth cycle?**
#
# Your puzzle answer was `247`.

# %%
input = """.#.
..#
###"""

# %%
input = """...#..#.
..##.##.
..#.....
....#...
#.##...#
####..##
...##.#.
#.#.#..."""

# %%
from collections import Counter
from itertools import product

def get_neighbors(cell):
    neighbors = [tuple(cell[i] + v[i] for i in range(len(cell))) for v in product([-1, 0, 1], repeat=len(cell))]
    neighbors.remove(cell)
    return neighbors

def run_game(initial, cycles):
    alive = initial
    for cycle in range(cycles):
        neighbors = Counter(n for cell in alive for n in get_neighbors(cell))
        alive = [cell for cell, neighborCount in filter(lambda x: x[1] == 3 or x[0] in alive and x[1] == 2, neighbors.items())]
    return alive

inital = [(x, y, 0) for x, line in enumerate(input.split("\n")) for y, _ in filter(lambda c: c[1] == '#', enumerate(line))]

len(run_game(inital, 6))

# %% [markdown]
# ### Part Two
#
# For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has **four spatial dimensions**, not three.
#
# The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (`x`, `y`, `z`, `w`), there exists a single cube (really, a **hypercube**) which is still either **active** or **inactive**.
#
# Each cube only ever considers its **neighbors**: any of the `80` other cubes where any of their coordinates differ by at most `1`. For example, given the cube at `x=1,y=2,z=3,w=4`, its neighbors include the cube at `x=2,y=2,z=3,w=3`, the cube at `x=0,y=2,z=3,w=4`, and so on.
#
# The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the **number of active neighbors** of each cube.
#
# For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given `z` and `w` coordinate:
#
# Before any cycles:
#
# z=0, w=0
#
#     .#.
#     ..#
#     ###
#
# After 1 cycle:
#
#     z=-1, w=-1
#     #..
#     ..#
#     .#.
#
#     z=0, w=-1
#     #..
#     ..#
#     .#.
#
#     z=1, w=-1
#     #..
#     ..#
#     .#.
#
#     z=-1, w=0
#     #..
#     ..#
#     .#.
#
#     z=0, w=0
#     #.#
#     .##
#     .#.
#
#     z=1, w=0
#     #..
#     ..#
#     .#.
#
#     z=-1, w=1
#     #..
#     ..#
#     .#.
#
#     z=0, w=1
#     #..
#     ..#
#     .#.
#
#     z=1, w=1
#     #..
#     ..#
#     .#.
#
#
# After 2 cycles:
#
#     z=-2, w=-2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-1, w=-2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=-2
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=1, w=-2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=-2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-2, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-1, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=1, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=-1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-2, w=0
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=-1, w=0
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=0
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=1, w=0
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=0
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=-2, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-1, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=1, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=1
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=-2, w=2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
#     z=-1, w=2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=0, w=2
#     ###..
#     ##.##
#     #...#
#     .#..#
#     .###.
#
#     z=1, w=2
#     .....
#     .....
#     .....
#     .....
#     .....
#
#     z=2, w=2
#     .....
#     .....
#     ..#..
#     .....
#     .....
#
# After the full six-cycle boot process completes, `848` cubes are left in the **active** state.
#
# Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. **How many cubes are left in the active state after the sixth cycle?**
#
# Your puzzle answer was `1392`.

# %%
inital = [(x, y, 0, 0) for x, line in enumerate(input.split("\n")) for y, _ in filter(lambda c: c[1] == '#', enumerate(line))]

len(run_game(inital, 6))
