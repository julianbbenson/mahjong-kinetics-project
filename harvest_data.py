import os
import json
import csv

# --- CONFIGURATION ---
# UPDATE THIS PATH TO YOUR DATA FOLDER
DATA_FOLDER = './riichi_data'
OUTPUT_FILE = 'kinetics_data.csv'


def harvest():
    print(f"Initializing HARVESTER in: {DATA_FOLDER}")

    total_files = 0
    riichis_found = 0

    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Header: GameID, Turn Number, [S] Tiles Left, Outcome (1=Win, 0=Fail)
        writer.writerow(['game_id', 'turn_number', 'tiles_left_at_riichi', 'outcome'])

        for root, dirs, files in os.walk(DATA_FOLDER):
            for filename in files:
                if filename.startswith('.'): continue

                filepath = os.path.join(root, filename)
                total_files += 1

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        wall_tiles = 70
                        current_turn = 0
                        riichi_players = {}

                        for line in f:
                            try:
                                event = json.loads(line)
                            except:
                                continue

                            evt_type = event.get('type')

                            if evt_type == 'start_kyoku':
                                wall_tiles = 70
                                current_turn = 0
                                riichi_players = {}

                            if evt_type == 'tsumo':
                                wall_tiles -= 1
                                current_turn += 1

                            if evt_type == 'reach':
                                actor = event.get('actor')
                                riichi_players[actor] = {
                                    'concentration': wall_tiles,
                                    'turn': current_turn
                                }
                                riichis_found += 1

                            if evt_type == 'hora':
                                winner = event.get('actor')
                                if winner in riichi_players:
                                    data = riichi_players[winner]
                                    writer.writerow([filename, data['turn'], data['concentration'], 1])
                                    del riichi_players[winner]

                            if evt_type == 'end_kyoku':
                                for actor, data in riichi_players.items():
                                    writer.writerow([filename, data['turn'], data['concentration'], 0])
                                riichi_players = {}

                except Exception:
                    continue

                if total_files % 1000 == 0:
                    print(f"Scanned {total_files} files... Riichis Found: {riichis_found}")

    print("-" * 30)
    print(f"MISSION COMPLETE.")
    print(f"Total Files: {total_files}")
    print(f"Riichis Found: {riichis_found}")
    print(f"Data saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    harvest()