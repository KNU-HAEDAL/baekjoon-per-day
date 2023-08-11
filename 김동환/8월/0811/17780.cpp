#include <bits/stdc++.h>
#define INF 987654321
typedef long long ll;
using namespace std;

#define WHITE 0
#define RED 1
#define BLUE 2


int n, k;
int colors[13][13];
vector<int> board[13][13];
vector<pair<pair<int, int>, int>> pieces;
int dy[] = {0, 0, -1, 1}, dx[] = {1, -1, 0, 0};

bool isInside(int y, int x) {
  return 0 <= y and y < n and 0 <= x and x < n;
}

void setPieces(int id, int y, int x, int dir) {
  pieces[id].first.first = y;
  pieces[id].first.second = x;
  pieces[id].second = dir;
}

int solve() {
  for(int time = 1; time <= 1000; time++) {
    for(int piece = 0; piece < k; piece++) {
      int y = pieces[piece].first.first;
      int x = pieces[piece].first.second;
      int dir = pieces[piece].second;

      if (board[y][x][0] != piece) {
        continue;
      }

      int ny = y + dy[dir];
      int nx = x + dx[dir];

      if (not isInside(ny, nx) or colors[ny][nx] == BLUE) {
        if (dir <= 1) {
          dir = (dir + 1) % 2;
        }
        else {
          dir = ((dir - 2 + 1) % 2) + 2;
        }

        setPieces(piece, y, x, dir);
        ny = y + dy[dir];
        nx = x + dx[dir];
      }

      if (not isInside(ny, nx) or colors[ny][nx] == BLUE) {
        continue;
      }
      else if (colors[ny][nx] == WHITE) {
        int piecePos;
        for(int i = 0; i < board[y][x].size(); i++) {
          if (board[y][x][i] == piece) {
            piecePos = i;
            break;
          }
        }

        for(int i = piecePos; i < board[y][x].size(); i++) {
          int movedPiece = board[y][x][i];
          board[ny][nx].push_back(movedPiece);
          setPieces(movedPiece, ny, nx, pieces[movedPiece].second);
        }

        board[y][x].resize(piecePos);
      }
      else {
        int piecePos;
        for(int i = board[y][x].size() - 1; i >= 0; i--) {
          int movedPiece = board[y][x][i];
          board[ny][nx].push_back(movedPiece);
          setPieces(movedPiece, ny, nx, pieces[movedPiece].second);

          if (movedPiece == piece) {
            piecePos = i;
            break;
          }
        }

        board[y][x].resize(piecePos);
      }

      if (board[ny][nx].size() >= 4) {
        return time;
      }
    }
  }

  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  cin >> n >> k;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> colors[i][j];
    }
  }

  for(int i = 0; i < k; i++) {
    int y, x, dir;
    cin >> y >> x >> dir;

    pieces.push_back({{y - 1, x - 1}, dir - 1});
    board[y - 1][x - 1].push_back(i);
  }

  cout << solve() << endl;

  return 0;
}
