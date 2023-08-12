#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;

#define END_CELL 21

int dice[10], piece[4];
vector<int> board[33];
int boardScore[33];
int maxScore = 0;

void solve(int curDice, int curScore) {
  maxScore = max(maxScore, curScore);

  if (curDice == 10) {
    return;
  }

  for(int i = 0; i < 4; i++) {
    int curPos = piece[i];

    // 현재 도착 칸에 있다면 넘김
    if (curPos == END_CELL) {
      continue;
    }

    // 처음 시작이 파란 칸이면 파란색 화살표, 빨간 색이면 빨간색 화살표로 이동함.
    int nextPos = board[curPos][board[curPos].size() - 1];
    for(int j = 1; j < dice[curDice]; j++) {
      if (nextPos == END_CELL) {
        break;
      }

      nextPos = board[nextPos][0];
    }

    bool isAlreadyOtherPiece = false;
    for(int j = 0; j < 4; j++) {
      if (nextPos != END_CELL and piece[j] == nextPos) {
        isAlreadyOtherPiece = true;
        break;
      }
    }
    if (isAlreadyOtherPiece) {
      continue;
    }

    piece[i] = nextPos;

    solve(curDice + 1, curScore + boardScore[nextPos]);

    piece[i] = curPos;
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  for(int i = 0; i <= 20; i++) {
    board[i].push_back(i + 1);
    boardScore[i] = i * 2;
  }
  board[5].push_back(22);
  board[22].push_back(23);
  board[23].push_back(24);
  board[24].push_back(30);
  boardScore[22] = 13;
  boardScore[23] = 16;
  boardScore[24] = 19;

  board[10].push_back(25);
  board[25].push_back(26);
  board[26].push_back(30);
  boardScore[25] = 22;
  boardScore[26] = 24;

  board[15].push_back(27);
  board[27].push_back(28);
  board[28].push_back(29);
  board[29].push_back(30);
  boardScore[27] = 28;
  boardScore[28] = 27;
  boardScore[29] = 26;

  board[30].push_back(31);
  board[31].push_back(32);
  board[32].push_back(20);
  boardScore[30] = 25;
  boardScore[31] = 30;
  boardScore[32] = 35;

  for(int i = 0; i < 10; i++) {
    cin >> dice[i];
  }

  solve(0, 0);
  cout << maxScore << endl;

  return 0;
}
