# BlackWhite

The Number Game is a simple two-player game where players take turns selecting numbers from a predefined range. The goal is to accumulate points based on the numbers chosen and determine the winner based on the final scores.

## Introduction

Welcome to BlackWhite! This game challenges your number selection skills and strategic thinking. Play against a friend and see who can achieve the highest score!

## How to Play

1. Run the `game.py` file to start the game.
    ```shell
   python game.py
   ```

2. Each player takes turns entering a number within the allowed range. The maximum number is determined by the current round. For the first 9 rounds, the maximum number is 99. In the bonus round, the maximum number is reduced to 33.

3. After each player enters a number, the selected number and the remaining range for that player are displayed.

4. At the end of each round, the round winner is announced, and the scores are updated.

5. The game continues until a player reaches the winning score or the bonus round is completed.

## Game Rules

- Each player can choose a number within the remaining range of available numbers. If a player tries to select a number greater than the available range, it will be adjusted to the maximum available number.

- In case of a draw, no points are awarded, and the round is considered a tie.

- The player who wins the round gets one point added to their score.

- After each round, the current scores are displayed.

- If a player reaches a score of 5 before the 9th round, they are declared the winner of the game.

- If the 9th round is completed and there is no winner yet, a bonus round is initiated.

- In the bonus round, the players will play three additional rounds with a maximum number of 33. The winner of the bonus round is determined by comparing the final scores.

- The player with the higher score at the end of the game is declared the overall winner.

## File Description

- `number_game.py`: The main Python script that implements the Number Game. Run this file to start the game.

- `README.md`: This file provides instructions and information about the game.

## Requirements

- Python 3.x

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


# BlackWhite

흑과 백 게임은 두 명의 플레이어가 정해진 범위 내에서 숫자를 선택하며 번갈아가며 진행하는 간단한 두 명용 게임입니다. 목표는 선택된 숫자에 기반하여 점수를 누적하고 최종 점수를 기준으로 승자를 결정하는 것입니다.

## 게임 방법

1. `game.py` 파일을 실행하여 게임을 시작합니다.
    ```shell
    python game.py
    ```

2. 각 플레이어는 허용 범위 내에서 숫자를 입력하는 순서대로 차례를 진행합니다. 최대 숫자는 현재 라운드에 따라 결정됩니다. 처음 9라운드에서는 최대 숫자가 99이며, 보너스 라운드에서는 최대 숫자가 33으로 감소합니다.

3. 각 플레이어가 숫자를 입력한 후 해당 플레이어의 선택한 숫자와 남은 범위가 표시됩니다.

4. 각 라운드가 끝날 때마다 라운드 승자가 발표되고 점수가 업데이트됩니다.

5. 한 플레이어가 승리 점수에 도달하거나 보너스 라운드가 완료될 때까지 게임은 계속됩니다.

## 게임 규칙

- 각 플레이어는 가능한 숫자 범위 내에서 숫자를 선택할 수 있습니다. 플레이어가 가능한 범위를 초과하여 숫자를 선택하려고 하면 가능한 최대 숫자로 조정됩니다.

- 무승부인 경우 점수는 주어지지 않으며 해당 라운드는 무승부로 간주됩니다.

- 라운드에서 이긴 플레이어는 점수에 1점이 추가됩니다.

- 각 라운드가 끝난 후 현재 점수가 표시됩니다.

- 9라운드 이전에 플레이어가 5점을 얻으면 게임에서 승리합니다.

- 9라운드가 완료되고 아직 승자가 없는 경우 보너스 라운드가 시작됩니다.

- 보너스 라운드에서 플레이어는 최대 숫자가 33인 추가적인 3라운드를 진행합니다. 보너스 라운드의 승자는 최종 점수를 비교하여 결정됩니다.

- 게임이 종료되면 점수가 더 높은 플레이어가 전체적인 승자로 선언됩니다.

## 파일 설명

- `game.py`: 게임을 실행하기 위한 파일입니다. 이 파일을 실행하여 흑과 백 게임을 시작할 수 있습니다.
