# General

You can use your preferred programming language, pseudo code, or english to answer.

## 1) Traversing a List of Nodes

**Problem:** Given a list of Nodes where each Node can have a list of Nodes, how would you visit all the Nodes?

**Answer:** Implemented in General.py. I would generally use recursion for tree like structures.

## 2) Calculating Distance Between Tree Nodes

**Problem:** Given two nodes in a tree, how would you calculate the distance between them? (feel free to modify the data structures involved if it makes the calculation easier)

**Answer:** Implemented in General.py. I couldn't remember how to write any existing optimized search algorithms so I just wrote my own. 

I wrote a function to find the path from root to given node and return a list of the child indexes to get from root to node. Then I took the max path between node 1 and node 2, which would be the length of both paths summed.

From there I looped through and removed from the initial max steps where the node paths shared a value. There's definitely room for improvement, and in practice I would use an existing algorithm rather than making my own since an existing one would be faster and more proven. 

The last time I wrote a search algorithm was when I made a randomly generated tower defense game where I needed the map to generate differently every time, and I just used an existing algorithm.

## 3) Most Challenging Coding Project

**Problem:** Describe how you implemented your most challenging coding project. What was tricky about it?

**Answer:** When it comes to web development, I haven't had any huge challenges recently. My coding challenges recently have been more self-imposed and more data science and machine learning related on personal projects.

A couple weekends ago I challenged myself to start writing a S&P 500 (SPY) predictive model and to build it with new tech (to me) which I hadn't used before or in a long time. I leaned heavily on Github Copilot with Claude 3.7 Sonnet to get the basic setup for Django and Postgres projects.

I built basic data ingestors from Alpaca to get stock historical data and with FRED and yfinance to get historical values of VIX (volatility index) and US10Y bond rates, which went smoothly.

Then I experimented with various models, trying to optimize parameters and features to get a high confidence prediction for whether SPY would move up 0.5% from open price first or down 0.5% first. That took me Friday evening and most of Saturday.

I spent all of Sunday trying to recall my limited Django knowledge while setting up a basic GUI dashboard to run the model from. I think websockets was the hardest part since I hadn't used them before. I kept getting issues with asyncio collisions since Django's consumers used Asyncio and the Alpaca websocket for live stock data also used it behind the scenes. Ultimately, I ended up just writing my own implementation since I only needed to hit one websocket endpoint.

I don't know if that is my most difficult/challenging coding project, but recency makes it easier to write out. Ultimately, I get past challenges by not taking no for an answer and not being willing to "lose" to the code. I leverage AI tools, tutorials, and whatever else I need to understand the problem and weather my own frustration as best as I can and usually get it done.

# Javscript
I assume this should be done without testing code?
## 1) What's wrong with this if anything?

### Sources
[Next() without returns?](https://stackoverflow.com/questions/13133071/express-next-function-what-is-it-really-for)

1. `function( req, res, next ) =>` doesn't need the =>, or I'm pretty sure just dropping the `function` would work too
2. `if (err) next( new Error 'failed' )` still would return res.json with status 200 afterwards I believe

Otherwise I'm not seeing anything jumping out to me.

## 2) Copying Consts

```javascript
const src = {
    id : 12,
    name : 'Mr Wiggles',
    values : [ { x : 1, y : 3 }, { x : 100, y : 2.1 }, ... ],
    alternates : { id : 16, alias : 'Wig' },
    history : [ ... ]
}
```

`const src2 = {...src, name: 'Mrs Wiggles'}`

```javascript
const src3 = {
    ...src,
    values: src.values.map((val, ind) => {
        ind == 1 ? { ...val, x: 200 } : val
    })
}
```
or
```javascript
let src3 = {...src}
src3.values[1].x = 200
```

## 3) Delete an entry?

Object: `let foo = { x: 1, y: 2 }`

To delete x: `delete foo.x`

If it's a const, I would probably say it just shouldn't be a const if you need to delete things.

## 4) How do you delete an item from an Array, like 2 from [1,2,3]
Had to look this one up to remember the function.

`foo.splice(1, 1)`

## 5) What is the difference between the forEach and the for-loop implementation?
I don't see any functional difference. The forEach gives index and value where index isn't needed (except for assignment to data arr) and the for loop uses index to access value.

## 6) How would you modify the above code?
I think it would already do that, but there would be holes where errors occurred.

Had to do a jsfiddle to be sure (ind 0-9 are undefined)
```
let arr = []
arr[10] = 'hey'
console.log(arr)
```

## 7) What is wrong  with the class?

`.width` is a func and a value, but I don't remember if JS would complain about that since they can be accessed differently: `foo.width` vs `foo.width()`. Either way probably not good practice.

# Database Questions
## 1) Customer, product, transactions database structure

```sql
CREATE TABLE customers (
    id BIGINT PRIMARY KEY,
    first_name varchar(50),
    last_name varrchar(50)
)

CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    product_name varchar(50)
)

CREATE TABLE transactions (
    id BIGINT PRIMARY KEY,
    product_id BIGINT NOT NULL,
    customer_id BIGINT NOT NULL,
    --- other metadata, like total, date placed, etc.
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    FOREIGN KEY (product_id) REFERENCES products(id)
)
```

## 2) Delete all but most recent 30

Was going to do this but realized it was not right
```sql
DELETE FROM
    testtable
ORDER BY time DESC
LIMIT 30
```

I think this would work. I'd have it working in short order if I had the db to test on.
```sql
DELETE FROM
    testtable
WHERE
    id NOT IN (SELECT id FROM testtable ORDER BY time ASC LIMIT 30)
```

## 3) What is wrong with it?

I don't know the syntax for mysql package here, but the query seems wrong.

```sql
SELECT
    * AS everything
FROM
    {TABLENAME}
WHERE
    time < {VALUE}
```

As far as I know you can't alias * select.
Also, the query call should be async or use a promise I would assume and the cb param is never used.

There is potential for SQL injection here if it is an api route.

For the rest I'll do a quick search on mysql package in JS.

Seems like connection setup is fine, but it looks like I was right about the async need for the query call. Something like this? (also realized that mysql.query should be connection.query)

```javascript
connection.query(query, [tableName, value], (err, res) => {
    if (err) {
        // do something
    }
    return results
})
```

# React Questions
## 1) What's wrong give solutions
I haven't written React as non functional components for a while, so I had to do some Copilot prompts to refresh my memory.

That said the `<Button>` component is not imported so that is an issue and neither is React, but maybe those are assumed. The function call for onClick would also continuously call without clicking I think.

After research: `onButtonClick` might need to be an arrow function for definition or on call. The constructor likely isn't needed unless states are going to be used.

```javascript
onButtonClick = () => {}

// Or

onClick={() => this.onButtonClick()}
```

Final like this:
```javascript
import React from 'react';
import Button from 'some-button-library'; // Replace with actual button import

class MyPane extends React.Component {
  onButtonClick = () => {
    // do stuff
  }
  
  render() {
    return (
      <Button onClick={this.onButtonClick}>Click Me</Button>
    );
  }
}

export default MyPane;
```

I would write it like this (unless company practice is to use class based):

```javascript
import Button from 'somewhere'

const MyPane () => {
    const onButtonClick = () => {
        // do stuff
    }

    return (
        <Button
            onClick={onButtonClick}
        >
            Click Me
        </Button>
    )
}
```

Personally I prefer the second. Shorter code, same effect.

## 2)

I assume I don't need to build out a whole audio player and streamer and just the display?

This is one where I would have Github Copilot write it for me and then I would clean it up so that's what I did here. It also added a scruber. All I did was change styling. I chose TypeScript just to showcase it.

Functional:
```typescript
import { useState, useEffect, useRef, ChangeEvent } from 'react';

interface Song {
  name: string;
  duration: number;
}

interface CurrentSong extends Song {
  currentTime: number;
}

const SONGS: Song[] = [
  { name: 'song 1', duration: 60 },
  { name: 'song 2', duration: 120 },
];

const Player: React.FC = () => {
  const [currentSong, setCurrentSong] = useState<CurrentSong | null>(null);
  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const intervalRef = useRef<number | null>(null);

  // Toggle play/pause
  const togglePlayPause = (): void => {
    if (!currentSong) {
      // If no song is selected, play the first one
      setCurrentSong({ ...SONGS[0], currentTime: 0 });
      setIsPlaying(true);
      return;
    }
    setIsPlaying(!isPlaying);
  };

  // Update the current time of the song
  const updateSlider = (e: ChangeEvent<HTMLInputElement>): void => {
    if (currentSong) {
      setCurrentSong({
        ...currentSong,
        currentTime: parseInt(e.target.value)
      });
    }
  };

  // Format seconds to mm:ss
  const formatTime = (seconds: number): string => {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  // Effect to update song time when playing
  useEffect(() => {
    if (isPlaying && currentSong) {
      intervalRef.current = window.setInterval(() => {
        setCurrentSong(prev => {
          if (!prev) return null;
          
          if (prev.currentTime >= prev.duration) {
            clearInterval(intervalRef.current!);
            setIsPlaying(false);
            return prev;
          }
          
          return { ...prev, currentTime: prev.currentTime + 1 };
        });
      }, 1000);
    } else if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [isPlaying, currentSong]);

  return (
    <div style={styles.playerContainer}>
      <div style={styles.songInfo}>
        {currentSong ? (
          <h3>{currentSong.name}</h3>
        ) : (
          <h3>No song selected</h3>
        )}
      </div>
      
      <div style={styles.controls}>
        <button 
          style={styles.playButton} 
          onClick={togglePlayPause}
        >
          {isPlaying ? '⏸️' : '▶️'}
        </button>
      </div>
      
      <div style={styles.progressContainer}>
        <span>{currentSong ? formatTime(currentSong.currentTime) : '0:00'}</span>
        <input
          type="range"
          min="0"
          max={currentSong?.duration || 100}
          value={currentSong?.currentTime || 0}
          onChange={updateSlider}
          style={styles.slider}
          disabled={!currentSong}
        />
        <span>{currentSong ? formatTime(currentSong.duration) : '0:00'}</span>
      </div>
    </div>
  );
};

// Styles object
const styles = {
  playerContainer: {
    width: '350px',
    padding: '15px',
    borderRadius: '10px',
    backgroundColor: '#f5f5f5',
    boxShadow: '0 2px 10px rgba(0, 0, 0, 0.1)',
    fontFamily: 'Arial, sans-serif',
  },
  songInfo: {
    textAlign: 'center' as const,
    marginBottom: '15px',
  },
  controls: {
    display: 'flex',
    justifyContent: 'center' as const,
    alignItems: 'center' as const,
    marginBottom: '15px',
  },
  playButton: {
    width: '50px',
    height: '50px',
    fontSize: '24px',
    cursor: 'pointer',
    display: 'flex',
    justifyContent: 'center' as const,
    alignItems: 'center' as const,
  },
  progressContainer: {
    display: 'flex',
    alignItems: 'center' as const,
    marginBottom: '20px',
  },
  slider: {
    flex: 1,
    margin: '0 10px',
    height: '5px',
  },
};

export default Player;
```