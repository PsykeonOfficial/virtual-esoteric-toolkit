'''
The Virtual Esoteric Toolkit - A virtual toolkit for the modern occultist.
Copyright (C) 2025 Nikodemus of Psykeon
https://github.com/PsykeonOfficial/virtual-esoteric-toolkit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# Virtual Esoteric Toolkit
import os
import random
import time
from datetime import datetime, timedelta
from skyfield.api import load, Topos
import math

# ANSI color codes
RED, RESET = "\033[0;31m", "\033[0m"

# Override print and input for colored output
def colored_print(*args, **kwargs):
    print(f"{RED}", end="")
    print(*args, **kwargs)
    print(f"{RESET}", end="")

def colored_input(prompt=""):
    return input(f"{RED}{prompt}{RESET}")

# Clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu
def menu():
    while True:
        clear_terminal()
        colored_print("\n~ The Virtual Esoteric Toolkit ~")
        colored_print("By Nikodemus of Psykeon")
        colored_print("\nDivination Tools")
        colored_print("1. Tarot Deck\n2. Rune Set\n3. Coin Toss\n4. Dice Set\n5. I-Ching")
        colored_print("\nEsoteric Calculators")
        colored_print("6. Birth Chart\n7. Planetary Positions\n8. Moon Phases\n9. Numerology\n10. Sigil Base Extractor")
        colored_print("\nX. Quit\n")
        
        choice = colored_input("Select (1-10, X): ").strip().upper()
        if choice == "X":
            colored_print("\nThank you for using The Virtual Esoteric Toolkit.")
            time.sleep(3)
            break
        actions = {
            "1": tarot, "2": runes, "3": coin, "4": dice, "5": iching,
            "6": birthchart, "7": planets, "8": moon, "9": numerology, "10": createsigil
        }
        if choice in actions:
            actions[choice]()
        else:
            colored_print("Invalid selection.")

# Tarot Deck
def tarot():
    clear_terminal()
    tarot_deck = [
        f"{i} - {name}" for i, name in enumerate([
            "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
            "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
            "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
            "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement",
            "The World"] + [f"{n} of {suit}" for suit in ["Cups", "Pentacles", "Swords", "Wands"]
                           for n in ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]
        ])
    ]
    
    def draw_card(available_cards, use_reversals):
        card = random.choice(available_cards)
        return card + (" (Reversed)" if use_reversals and random.choice([True, False]) else "")
    
    colored_print("\nVirtual Tarot Deck")
    use_reversals = colored_input("\nUse reversals? (Y/N): ").strip().upper() == "Y"
    unlimited_draws = colored_input("\nUnlimited draws? (Y/N): ").strip().upper() == "Y"
    available_cards = tarot_deck.copy()
    colored_print("\n[Enter] to draw, [R] to reset, [M] for menu.\n")
    
    while True:
        command = colored_input().strip().upper()
        if command == 'R':
            return tarot()
        if command == "M":
            return menu()
        if command != '':
            colored_print("Invalid command.")
            continue
        if not unlimited_draws and not available_cards:
            message = "No More Cards to Draw"
            colored_print(f"+{'-' * (len(message) + 2)}+\n| {message} |\n+{'-' * (len(message) + 2)}+")
            continue
        card = draw_card(available_cards, use_reversals)
        if not unlimited_draws:
            available_cards.remove(card.split(" (")[0])
        colored_print(f"+{'-' * (len(card) + 2)}+\n| {card} |\n+{'-' * (len(card) + 2)}+")

# Rune Set
def runes():
    clear_terminal()
    runes_set = [
        f"{r} - {n}" for r, n in [
            ("ᚠ", "Fehu"), ("ᚢ", "Uruz"), ("ᚦ", "Thurisaz"), ("ᚨ", "Ansuz"), ("ᚱ", "Raidho"),
            ("ᚲ", "Kenaz"), ("ᚷ", "Gebo"), ("ᚹ", "Wunjo"), ("ᚺ", "Hagalaz"), ("ᚾ", "Nauthiz"),
            ("ᛁ", "Isa"), ("ᛃ", "Jera"), ("ᛇ", "Eihwaz"), ("ᛈ", "Perthro"), ("ᛉ", "Algiz"),
            ("ᛋ", "Sowilo"), ("ᛏ", "Tiwaz"), ("ᛒ", "Berkano"), ("ᛖ", "Ehwaz"), ("ᛗ", "Mannaz"),
            ("ᛚ", "Laguz"), ("ᛜ", "Ingwaz"), ("ᛞ", "Dagaz"), ("ᛟ", "Othala")
        ]
    ]
    
    def draw_rune(available_runes, use_reversals):
        rune = random.choice(available_runes)
        return rune + (" (Reversed)" if use_reversals and random.choice([True, False]) else "")
    
    colored_print("\nVirtual Runes Set")
    use_reversals = colored_input("\nUse reversals? (Y/N): ").strip().upper() == "Y"
    unlimited_runes = colored_input("\nUnlimited draws? (Y/N): ").strip().upper() == "Y"
    available_runes = runes_set.copy()
    colored_print("\n[Enter] to draw, [R] to reset, [M] for menu.\n")
    
    while True:
        command = colored_input().strip().upper()
        if command == 'R':
            return runes()
        if command == "M":
            return menu()
        if command != '':
            colored_print("Invalid command.")
            continue
        if not unlimited_runes and not available_runes:
            message = "No More Runes to Draw"
            colored_print(f"+{'-' * (len(message) + 2)}+\n| {message} |\n+{'-' * (len(message) + 2)}+")
            continue
        rune = draw_rune(available_runes, use_reversals)
        if not unlimited_runes:
            available_runes.remove(rune.split(" (")[0])
        colored_print(f"+{'-' * (len(rune) + 2)}+\n| {rune} |\n+{'-' * (len(rune) + 2)}+")

# Coin Toss
def coin():
    clear_terminal()
    results_log = []
    colored_print("\nVirtual Coin Toss")
    colored_print("\n[Enter] to toss, [R] to reset, [M] for menu.\n")
    
    while True:
        command = colored_input().strip().upper()
        if command == 'R':
            return coin()
        if command == "M":
            return menu()
        result = random.choice(["Heads", "Tails"])
        results_log.append(result)
        total = len(results_log)
        heads = results_log.count("Heads")
        tails = total - heads
        colored_print(f"Result: {result}")
        colored_print(f"Heads: {heads/total*100:.2f}% (n={heads}), Tails: {tails/total*100:.2f}% (n={tails}), Total: {total}")

# Dice Set
def dice():
    clear_terminal()
    total_sum = 0
    valid_dice = {'d4': 4, 'd6': 6, 'd8': 8, 'd10': 10, 'd12': 12, 'd20': 20}
    
    def roll_dice(dice_selection):
        nonlocal total_sum
        roll_total = 0
        for sides, count in dice_selection:
            rolls = [random.randint(1, sides) for _ in range(count)]
            roll_total += sum(rolls)
            colored_print(f"{count} x d{sides}: {rolls} (Total: {sum(rolls)})")
        total_sum += roll_total
        colored_print(f"Overall Total: {total_sum}")
        colored_print("\n[Enter] to roll, [R] to change dice, [M] for menu.")
        
        while True:
            command = colored_input().strip().upper()
            if command == 'R':
                clear_terminal()
                return choose_dice()
            if command == 'M':
                return menu()
            if command == '':
                return roll_dice(dice_selection)
            colored_print("Invalid command.")
    
    def choose_dice():
        nonlocal total_sum
        total_sum = 0
        colored_print("\nVirtual Dice Set")
        colored_print("\nChoose dice (e.g., d6(2),d8(3)) or [M] for menu.")
        
        while True:
            choice = colored_input().strip().lower()
            if choice == 'm':
                return menu()
            try:
                dice_selection = []
                for part in choice.split(','):
                    part = part.strip()
                    dice_type, count = part.split('(')
                    if dice_type not in valid_dice:
                        raise ValueError(f"Invalid dice: {dice_type}")
                    count = int(count[:-1])
                    dice_selection.append((valid_dice[dice_type], count))
                return roll_dice(dice_selection)
            except ValueError as e:
                colored_print(f"Invalid format: {e}")
    
    choose_dice()

# I-Ching
def iching():
    clear_terminal()
    hexagram_meanings = {
    '111111': '1. 乾 Qián - The Creative - Strong action, leadership, and creative power.',
    '000000': '2. 坤 Kūn - The Receptive - Yielding, nurturing, and devotion.',
    '100010': '3. 屯 Zhūn - Difficulty at the Beginning - Initial challenges, growth through perseverance.',
    '010001': '4. 蒙 Méng - Youthful Folly - Inexperience, learning through mistakes.',
    '111010': '5. 需 Xū - Waiting - Patience, timing, and preparation.',
    '010111': '6. 訟 Sòng - Conflict - Disagreement, seeking resolution.',
    '010000': '7. 師 Shī - The Army - Discipline, organization, and collective effort.',
    '000010': '8. 比 Bǐ - Holding Together - Union, cooperation, and support.',
    '111011': '9. 小畜 Xiǎo Chù - Small Taming - Gentle influence, small steps toward progress.',
    '110111': '10. 履 Lǚ - Treading - Caution, careful progress, and respect.',
    '111000': '11. 泰 Tài - Peace - Harmony, balance, and prosperity.',
    '000111': '12. 否 Pǐ - Standstill - Stagnation, lack of progress, and disconnection.',
    '101111': '13. 同人 Tóng Rén - Fellowship - Community, shared goals, and cooperation.',
    '111101': '14. 大有 Dà Yǒu - Great Possession - Abundance, responsibility, and wealth.',
    '001000': '15. 謙 Qiān - Modesty - Humility, simplicity, and balance.',
    '000100': '16. 豫 Yù - Enthusiasm - Joy, inspiration, and collective action.',
    '100110': '17. 隨 Suí - Following - Adaptation, following the flow, and flexibility.',
    '011001': '18. 蠱 Gǔ - Work on the Decayed - Repair, renewal, and addressing neglect.',
    '110000': '19. 臨 Lín - Approach - Nearing, preparation, and anticipation.',
    '000011': '20. 觀 Guān - Contemplation - Observation, reflection, and insight.',
    '100101': '21. 噬嗑 Shì Kè - Biting Through - Determination, overcoming obstacles.',
    '101001': '22. 賁 Bì - Grace - Beauty, elegance, and refinement.',
    '000001': '23. 剝 Bō - Splitting Apart - Decay, collapse, and letting go.',
    '100000': '24. 復 Fù - Return - Renewal, turning point, and new beginnings.',
    '100111': '25. 無妄 Wú Wàng - Innocence - Spontaneity, purity, and natural action.',
    '111001': '26. 大畜 Dà Chù - Great Taming - Restraint, potential, and controlled power.',
    '100001': '27. 頤 Yí - Nourishment - Sustenance, self-care, and growth.',
    '011110': '28. 大過 Dà Guò - Preponderance of the Great - Excess, critical point, and transition.',
    '010010': '29. 坎 Kǎn - The Abysmal - Danger, depth, and navigating challenges.',
    '101101': '30. 離 Lí - The Clinging - Brightness, clarity, and dependence.',
    '001110': '31. 咸 Xián - Influence - Attraction, influence, and mutual response.',
    '011100': '32. 恆 Héng - Duration - Perseverance, commitment, and stability.',
    '001111': '33. 遯 Dùn - Retreat - Withdrawal, strategic retreat, and conservation.',
    '111100': '34. 大壯 Dà Zhuàng - Great Power - Strength, assertiveness, and responsibility.',
    '000101': '35. 晉 Jìn - Progress - Advancement, growth, and flourishing.',
    '101000': '36. 明夷 Míng Yí - Darkening of the Light - Concealment, endurance, and inner light.',
    '101011': '37. 家人 Jiā Rén - The Family - Roles, relationships, and harmony at home.',
    '110101': '38. 睽 Kuí - Opposition - Contrast, tension, and misunderstanding.',
    '001010': '39. 蹇 Jiǎn - Obstruction - Obstacles, difficulty, and turning back.',
    '010100': '40. 解 Xiè - Deliverance - Release, forgiveness, and moving forward.',
    '110001': '41. 損 Sǔn - Decrease - Reduction, simplification, and lessening.',
    '100011': '42. 益 Yì - Increase - Growth, expansion, and augmentation.',
    '111110': '43. 夬 Guài - Breakthrough - Resolution, determination, and decisive action.',
    '011111': '44. 姤 Gòu - Coming to Meet - Encounter, temptation, and caution.',
    '000110': '45. 萃 Cuì - Gathering Together - Assembly, unity, and collective power.',
    '011000': '46. 升 Shēng - Pushing Upward - Effort, gradual progress, and ascent.',
    '010110': '47. 困 Kùn - Oppression - Exhaustion, adversity, and resilience.',
    '011010': '48. 井 Jǐng - The Well - Resources, sustenance, and community support.',
    '101110': '49. 革 Gé - Revolution - Change, transformation, and renewal.',
    '011101': '50. 鼎 Dǐng - The Cauldron - Nourishment, alchemy, and transformation.',
    '100100': '51. 震 Zhèn - The Arousing - Shock, awakening, and sudden change.',
    '001001': '52. 艮 Gèn - Keeping Still - Stillness, meditation, and inner peace.',
    '011011': '53. 漸 Jiàn - Development - Gradual progress, patience, and growth.',
    '100110': '54. 歸妹 Guī Mèi - The Marrying Maiden - Subordination, secondary roles, and caution.',
    '101100': '55. 豐 Fēng - Abundance - Fullness, prosperity, and peak moments.',
    '001101': '56. 旅 Lǚ - The Wanderer - Travel, transience, and adaptability.',
    '011011': '57. 巽 Xùn - The Gentle - Penetration, persistence, and subtle influence.',
    '110110': '58. 兌 Duì - The Joyous - Joy, pleasure, and open communication.',
    '011010': '59. 渙 Huàn - Dispersion - Dissolution, spreading, and reuniting.',
    '010110': '60. 節 Jié - Limitation - Boundaries, discipline, and moderation.',
    '110011': '61. 中孚 Zhōng Fú - Inner Truth - Sincerity, insight, and inner knowing.',
    '001100': '62. 小過 Xiǎo Guò - Small Preponderance - Attention to detail, caution, and small steps.',
    '101010': '63. 既濟 Jì Jì - After Completion - Completion, balance, and vigilance.',
    '010101': '64. 未濟 Wèi Jì - Before Completion - Transition, potential, and preparation.'
    }
    trigrams = {
        '111': 'Heaven (Qian) - Creative, Strong',
        '110': 'Lake (Dui) - Joyous, Open',
        '101': 'Fire (Li) - Clinging, Bright',
        '100': 'Thunder (Zhen) - Arousing, Active',
        '011': 'Wind (Xun) - Gentle, Penetrating',
        '010': 'Water (Kan) - Abysmal, Dangerous',
        '001': 'Mountain (Gen) - Still, Resting',
        '000': 'Earth (Kun) - Receptive, Yielding'
    }
    
    line_values = {
        6: "Broken (changing yin)",
        7: "Solid (static yang)",
        8: "Broken (static yin)",
        9: "Solid (changing yang)"
    }    

    
    def get_ascii(line, is_primary=True):
        if is_primary:
            return {
                6: "-- --x", 7: "-----", 8: "-- --", 9: "-----o"
            }.get(line, "Invalid")
        return {7: "-----", 8: "-- --"}.get(line, "Invalid")
    
    colored_print("\nVirtual I-Ching")
    while True:
        colored_print("\n[Enter] to start, [R] to reset, [M] for menu.")
        command = colored_input().strip().upper()
        if command == 'R':
            return iching()
        if command == 'M':
            return menu()
        if command != '':
            colored_print("Invalid command.")
            continue
        
        lines = []
        for i in range(1, 7):
            colored_print(f"\nLine {i}:")
            colored_input(f"Press Enter to toss coins for line {i}...")
            numbers = [random.choice([2, 3]) for _ in range(3)]
            line_sum = sum(numbers)
            coin_display = " + ".join(["Heads (3)" if n == 3 else "Tails (2)" for n in numbers])
            colored_print(f"Result: {coin_display} = {line_sum}")
            lines.append(line_sum)
        
        primary_ascii = [get_ascii(line) for line in lines]
        changing_lines = [i+1 for i, line in enumerate(lines) if line in [6, 9]]
        secondary_lines = [7 if line == 6 else 8 if line == 9 else line for line in lines]
        secondary_ascii = [get_ascii(line, False) for line in secondary_lines] if changing_lines else []
        
        primary_binary = ''.join('1' if line in [7, 9] else '0' for line in lines)
        colored_print("\nPrimary Hexagram:")
        for i in range(5, -1, -1):
            colored_print(f"Line {i+1}: {primary_ascii[i]}")
        colored_print(f"Binary: {primary_binary}")
        colored_print(f"Meaning: {hexagram_meanings.get(primary_binary, 'Unknown')}")
        colored_print(f"\nComposed of:")
        colored_print(f"  Lower trigram: {trigrams.get(primary_binary[:3], 'Unknown')}")
        colored_print(f"  Upper trigram: {trigrams.get(primary_binary[3:], 'Unknown')}")
        
        if secondary_ascii:
            secondary_binary = ''.join('1' if line in [7, 9] else '0' for line in secondary_lines)
            colored_print("\nSecondary Hexagram:")
            for i in range(5, -1, -1):
                colored_print(f"Line {i+1}: {secondary_ascii[i]}")
            colored_print(f"Binary: {secondary_binary}")
            colored_print(f"Meaning: {hexagram_meanings.get(secondary_binary, 'Unknown')}")
            colored_print(f"\nComposed of:")
            colored_print(f"  Lower trigram: {trigrams.get(secondary_binary[:3], 'Unknown')}")
            colored_print(f"  Upper trigram: {trigrams.get(secondary_binary[3:], 'Unknown')}")
        else:
            colored_print("\nNo secondary hexagram (no changing lines).")

# Birth Chart
def birthchart():
    clear_terminal()
    eph = load('de421.bsp')
    planets = {
        'Sun ☉': eph['sun'], 'Moon ☽': eph['moon'], 'Mercury ☿': eph['mercury'],
        'Venus ♀': eph['venus'], 'Mars ♂': eph['mars'], 'Jupiter ♃': eph['jupiter barycenter'],
        'Saturn ♄': eph['saturn barycenter'], 'Uranus ♅': eph['uranus barycenter'],
        'Neptune ♆': eph['neptune barycenter'], 'Pluto ♇': eph['pluto barycenter']
    }
    signs = ["Aries ♈", "Taurus ♉", "Gemini ♊", "Cancer ♋", "Leo ♌", "Virgo ♍",
             "Libra ♎", "Scorpio ♏", "Sagittarius ♐", "Capricorn ♑", "Aquarius ♒", "Pisces ♓"]
    
    def get_sign(degree):
        return signs[int(degree // 30) % 12]
    
    def calculate_positions(birth_datetime, latitude, longitude):
        location = Topos(latitude_degrees=latitude, longitude_degrees=longitude)
        ts = load.timescale()
        t = ts.utc(birth_datetime.year, birth_datetime.month, birth_datetime.day,
                  birth_datetime.hour, birth_datetime.minute)
        positions = {}
        for planet, obj in planets.items():
            astrometric = (eph['earth'] + location).at(t).observe(obj).apparent()
            x, y = astrometric.ecliptic_position().au[:2]
            degree = math.degrees(math.atan2(y, x)) % 360
            positions[planet] = f"{get_sign(degree)} ({degree:.2f}°)"
        return positions
    
    colored_print("\nVirtual Birth Chart")
    while True:
        colored_print("\n[Enter] to start, [R] to reset, [M] for menu.")
        choice = colored_input().strip().upper()
        if choice == 'R':
            return birthchart()
        if choice == 'M':
            return menu()
        if choice != '':
            colored_print("Invalid command.")
            continue
        try:
            year, month, day = map(int, colored_input("Birth date (YYYY MM DD): ").split())
            hour, minute = map(int, colored_input("Birth time (HH MM, 24-hour): ").split())
            latitude = float(colored_input("Latitude (e.g., 48.8566): "))
            longitude = float(colored_input("Longitude (e.g., 2.3522): "))
            chart = calculate_positions(datetime(year, month, day, hour, minute), latitude, longitude)
            colored_print("\nAstrological Birth Chart:")
            for planet, pos in chart.items():
                colored_print(f"{planet}: {pos}")
        except Exception as e:
            colored_print(f"Error: {e}")

# Planetary Positions
def planets():
    clear_terminal()
    eph = load('de421.bsp')
    earth = eph['earth']
    ts = load.timescale()
    celestial_info = {
        name: (symbol, eph[f"{name} {'barycenter' if name in ['jupiter', 'saturn', 'uranus', 'neptune', 'pluto'] else ''}".strip()])
        for name, symbol in [
            ('sun', '☉'), ('moon', '☽'), ('mercury', '☿'), ('venus', '♀'), ('earth', '⊕'),
            ('mars', '♂'), ('jupiter', '♃'), ('saturn', '♄'), ('uranus', '♅'), ('neptune', '♆'), ('pluto', '♇')
        ]
    }
    
    def calculate_positions():
        t = ts.now()
        return {
            name: (body.at(t).observe(earth).radec()[0].hours, body.at(t).observe(earth).radec()[1].degrees, symbol)
            for name, (symbol, body) in celestial_info.items()
        }
    
    colored_print("\nVirtual Planet Positions")
    while True:
        colored_print("\n[Enter] to start, [R] to reset, [M] for menu.")
        choice = colored_input().strip().upper()
        if choice == 'R':
            return planets()
        if choice == 'M':
            return menu()
        positions = calculate_positions()
        colored_print("\nCelestial Bodies Positions:")
        for name, (ra, dec, symbol) in positions.items():
            colored_print(f"{symbol} {name.capitalize()} at (RA: {ra:.2f}h, Dec: {dec:.2f}°)")

# Moon Phases
def moon():
    clear_terminal()
    planets = load('de421.bsp')
    earth, moon, sun = planets['earth'], planets['moon'], planets['sun']
    ts = load.timescale()
    
    def moon_phase(date):
        t = ts.utc(date.year, date.month, date.day)
        separation = moon.at(t).separation_from(sun.at(t)).degrees / 180.0
        phases = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
                  "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
        visuals = {"New Moon": "◯", "Waxing Crescent": "☽", "First Quarter": "◑", "Waxing Gibbous": "(",
                   "Full Moon": "●", "Waning Gibbous": ")", "Last Quarter": "◐", "Waning Crescent": "☾"}
        phase_index = int((separation * 8) % 8)
        return phases[phase_index], visuals[phases[phase_index]]
    
    def display_phases(start_date, end_date=None):
        current = start_date
        end = end_date or start_date
        while current <= end:
            phase, visual = moon_phase(current)
            colored_print(f"{current.strftime('%Y-%m-%d')}: {phase} {visual}")
            current += timedelta(days=1)
    
    def process_date(date_str):
        try:
            return datetime(*map(int, date_str.strip().split()))
        except ValueError:
            colored_print("Invalid date format. Use YYYY MM DD.")
            return None
    
    while True:
        colored_print("\nVirtual Moon Phases")
        colored_print("\nEnter date(s) (YYYY MM DD, or range with -), [R] to reset, or [M] for menu.")
        date_input = colored_input().strip().upper()
        if date_input == "M":
            return menu()
        if date_input == "R":
            colored_print("Resetting... Let's chase the moon again!")
            clear_terminal()
            continue
        if "-" in date_input:
            start, end = map(process_date, date_input.split("-"))
            if start and end:
                display_phases(start, end)
        elif "," in date_input:
            for date_str in date_input.split(","):
                date = process_date(date_str)
                if date:
                    display_phases(date)
        else:
            date = process_date(date_input)
            if date:
                display_phases(date)

# Numerology
def numerology():
    clear_terminal()
    meanings = {
        "life_path": {
                1: "Independence, Leadership",
                2: "Diplomacy, Partnership",
                3: "Creativity, Expression",
                4: "Stability, Hard work",
                5: "Freedom, Adaptability",
                6: "Responsibility, Harmony",
                7: "Spirituality, Introspection",
                8: "Power, Ambition",
                9: "Compassion, Humanitarianism",
                11: "Inspiration, Intuition",
                22: "Mastery, Vision",
                33: "Healing, Altruism"
            },
            "destiny": {
                1: "Leadership, Purpose",
                2: "Collaboration, Balance",
                3: "Joy, Creativity",
                4: "Foundation, Stability",
                5: "Change, Freedom",
                6: "Service, Family",
                7: "Wisdom, Solitude",
                8: "Power, Success",
                9: "Compassion, Service",
                11: "Visionary, Insight",
                22: "Master Builder, Potential",
                33: "Healing, Love"
            },
            "soul_urge": {
                1: "Self-Determination, Drive",
                2: "Peace, Harmony",
                3: "Expression, Joy",
                4: "Practicality, Security",
                5: "Adventure, Freedom",
                6: "Love, Care",
                7: "Mysticism, Depth",
                8: "Ambition, Power",
                9: "Humanitarianism, Idealism",
                11: "Inspiration, Intuition",
                22: "Mastery, Service",
                33: "Compassion, Healing"
            },
            "personality": {
                1: "Assertive, Strong",
                2: "Gentle, Diplomatic",
                3: "Outgoing, Charismatic",
                4: "Reliable, Practical",
                5: "Dynamic, Adaptable",
                6: "Nurturing, Caring",
                7: "Reserved, Analytical",
                8: "Confident, Ambitious",
                9: "Generous, Compassionate",
                11: "Creative, Charismatic",
                22: "Powerful, Authoritative",
                33: "Selfless, Inspirational"
            },
            "birthday": {
                1: "Leadership, Initiative",
                2: "Cooperation, Sensitivity",
                3: "Creativity, Joy",
                4: "Discipline, Order",
                5: "Freedom, Curiosity",
                6: "Nurturing, Responsibility",
                7: "Analysis, Contemplation",
                8: "Ambition, Material Success",
                9: "Humanitarian, Idealistic",
                11: "Intuitive, Spiritual Insight",
                22: "Mastery, Achievements",
                33: "Healing, Enlightenment"
            },
            "maturity": {
                1: "Individuality, Assertiveness",
                2: "Balance, Harmony",
                3: "Artistry, Communication",
                4: "Structure, Dependability",
                5: "Flexibility, Exploration",
                6: "Support, Family Focus",
                7: "Wisdom, Insight",
                8: "Power, Achievement",
                9: "Compassion, Sacrifice",
                11: "Visionary, Inspirational",
                22: "Strategic, Visionary",
                33: "Service, Love"
            },
            "personal_year": {
                1: "New Beginnings, Initiative",
                2: "Patience, Relationships",
                3: "Creativity, Socializing",
                4: "Stability, Hard Work",
                5: "Change, Adventure",
                6: "Family, Harmony",
                7: "Introspection, Spiritual Growth",
                8: "Power, Material Success",
                9: "Completion, Letting Go",
                11: "Intuition, Insight",
                22: "Mastery, Building",
                33: "Compassion, Global Awareness"
            }
        }
    
    def reduce(n):
        while n > 9 and n not in [11, 22, 33]:
            n = sum(int(d) for d in str(n))
        return n
    
    def calculate_life_path(birthdate):
        return reduce(sum(int(d) for d in birthdate.replace(" ", "")))
    
    def calculate_destiny(name):
        letter_values = {'a': 1, 'j': 1, 's': 1, 'b': 2, 'k': 2, 't': 2, 'c': 3, 'l': 3, 'u': 3,
                         'd': 4, 'm': 4, 'v': 4, 'e': 5, 'n': 5, 'w': 5, 'f': 6, 'o': 6, 'x': 6,
                         'g': 7, 'p': 7, 'y': 7, 'h': 8, 'q': 8, 'z': 8, 'i': 9, 'r': 9}
        return reduce(sum(letter_values.get(c, 0) for c in name.lower()))
    
    def calculate_soul_urge(name):
        letter_values = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3}
        return reduce(sum(letter_values.get(c, 0) for c in name.lower()))
    
    def calculate_personality(name):
        letter_values = {'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 1, 'k': 2, 'l': 3,
                         'm': 4, 'n': 5, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}
        consonants = ''.join(c for c in name.lower() if c not in 'aeiou ')
        return reduce(sum(letter_values.get(c, 0) for c in consonants))
    
    def calculate_birthday(birthdate):
        return reduce(int(birthdate.split()[2]))
    
    def calculate_maturity(life_path, destiny):
        return reduce(life_path + destiny)
    
    def calculate_personal_year(birthdate):
        year = datetime.now().year
        month_day = sum(int(d) for d in birthdate.split()[1:])
        return reduce(year + month_day)
    
    colored_print("\nVirtual Numerology Calculator")
    while True:
        colored_print("\n[Enter] to start, [R] to reset, [M] for menu.")
        choice = colored_input().strip().upper()
        if choice == 'R':
            return numerology()
        if choice == 'M':
            menu()
        if choice != '':
            colored_print("Invalid command.")
            continue
        
        birthdate = colored_input("Birthdate (YYYY MM DD): ")
        name = colored_input("Full name: ").strip()
        
        life_path = calculate_life_path(birthdate)
        destiny = calculate_destiny(name)
        soul_urge = calculate_soul_urge(name)
        personality = calculate_personality(name)
        birthday = calculate_birthday(birthdate)
        maturity = calculate_maturity(life_path, destiny)
        personal_year = calculate_personal_year(birthdate)
        
        colored_print("\n--- Numerology Report ---")
        for num, desc, type_ in [
            (life_path, "Life Path", "life_path"), (birthday, "Birthday", "birthday"),
            (destiny, "Destiny", "destiny"), (soul_urge, "Soul Urge", "soul_urge"),
            (personality, "Personality", "personality"), (maturity, "Maturity", "maturity"),
            (personal_year, "Personal Year", "personal_year")
        ]:
            colored_print(f"{desc} Number: {num} - {meanings.get(type_, {}).get(num, 'Unknown')}")

# Sigil Consonant Extractor
def createsigil():
    clear_terminal()
    colored_print("\nVirtual Sigil Consonant Extractor")
    while True:
        intention = colored_input("\nEnter intention, [R] to reset, [M] for menu: ").strip().upper()
        if intention == "R":
            return createsigil()
        if intention == "M":
            return menu()
        result = ''.join(sorted(set(c for c in intention if c.isalpha() and c not in 'AEIOU'), key=intention.index))
        colored_print(f"\nSigil consonants (no vowels, no repeats): {result}")

if __name__ == "__main__":
    menu()