#include <iostream>
#include <list>
#include <string>
#include <vector>

using namespace std;

int getThreeOfAKind(list<int> aDiceScore)
{
  vector<int> iDup;

  for(int i = 0; i < 6; i++)
  {
    iDup.push_back(0);
  }

  for(list<int>::iterator iter = aDiceScore.begin(); iter != aDiceScore.end(); ++iter)
  {
    if(*iter == 1)
      iDup[0]++;
    if(*iter == 2)
      iDup[1]++;
    if(*iter == 3)
      iDup[2]++;
    if(*iter == 4)
      iDup[3]++;
    if(*iter == 5)
      iDup[4]++;
    if(*iter == 6)
      iDup[5]++;
  }

  bool b = false;

  for(vector<int>::iterator it = iDup.begin(); it != iDup.end(); ++ it)
  {
    if (*it >= 3)
    {
      b = true;
      break;
    }
  }

  if(b)
  {
    int sum = 0;
    for(list<int>::iterator iter = aDiceScore.begin(); iter != aDiceScore.end(); ++iter)
    {
      sum += *iter;
    }
    return sum;
  }
  else
  {
    return 0;
  }
}

int getFourOfAKind(list<int> aDiceScore)
{
  vector<int> iDup;

  for(int i = 0; i < 6; i++)
  {
    iDup.push_back(0);
  }

  for(list<int>::iterator iter = aDiceScore.begin(); iter != aDiceScore.end(); ++iter)
  {
    if(*iter == 1)
      iDup[0]++;
    if(*iter == 2)
      iDup[1]++;
    if(*iter == 3)
      iDup[2]++;
    if(*iter == 4)
      iDup[3]++;
    if(*iter == 5)
      iDup[4]++;
    if(*iter == 6)
      iDup[5]++;
  }

  bool b = false;

  for(vector<int>::iterator it = iDup.begin(); it != iDup.end(); ++ it)
  {
    if (*it >= 4)
    {
      b = true;
      break;
    }
  }

  if(b)
  {
    int sum = 0;
    for(list<int>::iterator iter = aDiceScore.begin(); iter != aDiceScore.end(); ++iter)
    {
      sum += *iter;
    }
    return sum;
  }
  else
  {
    return 0;
  }
}

int getSmallStraight(list<int> aDiceScore)
{
  return 0;
}

int getLargeStraight(list<int> aDiceScore)
{
  return 0;
}

int getFullHouse(list<int> aDiceScore)
{
  return 0;
}

int getYahtzee(list<int> aDiceScore)
{
  return 0;
}

int getChance(list<int> aDiceScore)
{
  return 0;
}

list<int> RollDice()
{
  list<int> oneRollScore;
  return oneRollScore;
}

void printOneRoll(list<int> aDiceScores)
{
  cout << "printOneRoll" << endl;
}

bool testGetThreeOfAKind()
{
  list<int> aDiceScore1, aDiceScore2, aDiceScore3, aDiceScore4, aDiceScore5;
  aDiceScore1.push_back(1);
  aDiceScore1.push_back(2);
  aDiceScore1.push_back(3);
  aDiceScore1.push_back(4);
  aDiceScore1.push_back(5);

  aDiceScore2.push_back(1);
  aDiceScore2.push_back(1);
  aDiceScore2.push_back(1);
  aDiceScore2.push_back(4);
  aDiceScore2.push_back(4);

  aDiceScore3.push_back(2);
  aDiceScore3.push_back(2);
  aDiceScore3.push_back(1);
  aDiceScore3.push_back(2);
  aDiceScore3.push_back(4);

  aDiceScore4.push_back(3);
  aDiceScore4.push_back(3);
  aDiceScore4.push_back(3);
  aDiceScore4.push_back(3);
  aDiceScore4.push_back(5);

  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);

  bool b = true;

  b = b && getThreeOfAKind(aDiceScore1) == 0;
  b = b && getThreeOfAKind(aDiceScore2) == 11;
  b = b && getThreeOfAKind(aDiceScore3) == 11;
  b = b && getThreeOfAKind(aDiceScore4) == 17;
  b = b && getThreeOfAKind(aDiceScore5) == 25;

  return b;
}

bool testGetFourOfAKind()
{
  list<int> aDiceScore1, aDiceScore2, aDiceScore3, aDiceScore4, aDiceScore5;
  aDiceScore1.push_back(1);
  aDiceScore1.push_back(2);
  aDiceScore1.push_back(3);
  aDiceScore1.push_back(4);
  aDiceScore1.push_back(5);

  aDiceScore2.push_back(1);
  aDiceScore2.push_back(1);
  aDiceScore2.push_back(1);
  aDiceScore2.push_back(4);
  aDiceScore2.push_back(4);

  aDiceScore3.push_back(2);
  aDiceScore3.push_back(2);
  aDiceScore3.push_back(1);
  aDiceScore3.push_back(2);
  aDiceScore3.push_back(4);

  aDiceScore4.push_back(3);
  aDiceScore4.push_back(3);
  aDiceScore4.push_back(3);
  aDiceScore4.push_back(3);
  aDiceScore4.push_back(5);

  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);
  aDiceScore5.push_back(5);

  bool b = true;

  b = b && getFourOfAKind(aDiceScore1) == 0;
  b = b && getFourOfAKind(aDiceScore2) == 0;
  b = b && getFourOfAKind(aDiceScore3) == 0;
  b = b && getFourOfAKind(aDiceScore4) == 17;
  b = b && getFourOfAKind(aDiceScore5) == 25;

  return b;
}

int main(int argc, char const *argv[])
{
  string strResult = testGetThreeOfAKind() ? "True" : "False";
  cout << "getThreeOfAKind is running good? " << strResult << endl;

  strResult = testGetFourOfAKind() ? "True" : "False";
  cout << "getFourOfAKind is running good? " << strResult << endl;

  list<int> oneRollScore = RollDice();
  printOneRoll(oneRollScore);

  cout << "Another (y/n)";

  string strInput;
  cin >> strInput;

  while(true)
  {
    if("y" == strInput)
    {
      oneRollScore = RollDice();
      printOneRoll(oneRollScore);
      cout << "Another (y/n)";
      cin >> strInput;
    }
    else if("n" == strInput)
    {
      break;
    }
    else
    {
      cout << "Wrong input, Another (y/n)";
      cin >> strInput;
    }
  }

  return 0;
}
