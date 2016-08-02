var BOARD = [];
var ROWS, COLS;
var SQUARE_SIZE = 30;
var FRAME_RATE = 8;

var UP = 4;
var RIGHT = 1;
var DOWN = 2;
var LEFT = 3;

var PLAYER = [];
var food;
var EMPTY = 0, SNAKE = 1, FOOD = 2;
var DIR;

var GAME_OVER = false;

// 0 is nothing, 1 is snake head, 2 is snake body, 3 is food

function start() {
    COLS = 44;
    ROWS = 21;
    DIR = RIGHT;
    GAME_OVER = false;
    PLAYER = [ {x: Math.floor(COLS/2), y: Math.floor(ROWS/2)} ];
    BOARD = [];
    for(var i = 0; i < ROWS; i++){
        var arr = [];
        for(var j = 0; j < COLS; j++){
            arr.push(EMPTY);
        }
        BOARD.push(arr);
    }
    stroke(0, 255, 0);
}

function drawBoard() {
    BOARD = [];
    for(var i = 0; i < ROWS; i++){
        var arr = [];
        for(var j = 0; j < COLS; j++){
            arr.push(EMPTY);
        }
        BOARD.push(arr);
    }

    if(food){
        BOARD[food.y][food.x] = FOOD;
    }

    for(var i = 0; i < PLAYER.length; i++){
        BOARD[PLAYER[i].y][PLAYER[i].x] = SNAKE;
    }

    var a = PLAYER.pop();
    PLAYER.splice(1, 0, a);

    for(var y = 0; y < ROWS; y++){
        for(var x = 0; x < COLS; x++){
            if(BOARD[y][x] == EMPTY){
                fill(255);
            }
            else if(BOARD[y][x] == SNAKE){
                fill(0, 255, 0);
            }
            else if(BOARD[y][x] == FOOD){
                fill(255, 0, 0);
            }

            rect(x * SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE);
        }
    }
}

// place a food randomly in the board
function createFood() {
    food = {};
    food.x = Math.floor(random(COLS));
    food.y = Math.floor(random(ROWS));

    if(BOARD[food.y][food.x] == SNAKE){
        createFood();
    }
}

function setup() {
    frameRate(FRAME_RATE);
    start();
    createCanvas(COLS * SQUARE_SIZE+1, ROWS * SQUARE_SIZE+1);
    background(119, 120, 120);
    createFood();
}

function draw() {
    drawBoard();
    
    // player direction
    if ((key == 'd' || key == 'D' || keyCode == 39) && DIR != LEFT){
        DIR = RIGHT;
    }else if((key == 'a' || key == 'A' || keyCode == 37) && DIR != RIGHT){
        DIR = LEFT;
    }else if((key == 'w' || key == 'W' || keyCode == 38) && DIR != DOWN){
        DIR = UP;
    }else if((key == 's' || key == 'S' || keyCode == 40) && DIR != UP){
        DIR = DOWN;
    }
    // player movement
    if (GAME_OVER == false){
        if(DIR == RIGHT){
            if(PLAYER.length > 1){
                PLAYER[PLAYER.length-1].y = PLAYER[0].y;
                PLAYER[PLAYER.length-1].x = PLAYER[0].x;
            }
            PLAYER[0].x++;

            if(PLAYER[0].x > COLS){
                GAME_OVER = true;
            }else{
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    createFood();
                    PLAYER.push( { 
                        x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y 
                    } );
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){
                    GAME_OVER = true;
                }
            }
        }
        if(DIR == LEFT){
            if(PLAYER.length > 1){
                PLAYER[PLAYER.length -1].y = PLAYER[0].y;
                PLAYER[PLAYER.length -1].x = PLAYER[0].x;
            }
            PLAYER[0].x --;

            if(PLAYER[0].x < 0){
                GAME_OVER = true;
            }else{
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    createFood();
                    PLAYER.push( {x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y} );
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){
                    GAME_OVER = true;
                }
            }
        }
        if(DIR == UP){
            if(PLAYER.length > 1){
                PLAYER[PLAYER.length -1].y = PLAYER[0].y;
                PLAYER[PLAYER.length -1].x = PLAYER[0].x;
            }
            PLAYER[0].y --;
            if(PLAYER[0].y < 0){
                GAME_OVER = true;
            }else{
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    PLAYER.push( {x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y} );
                    createFood();
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){
                    GAME_OVER = true;
                }
            }
        }
        if(DIR == DOWN){
            if(PLAYER.length > 1){
                PLAYER[PLAYER.length -1].y = PLAYER[0].y;
                PLAYER[PLAYER.length -1].x = PLAYER[0].x;
            }
            PLAYER[0].y ++;
            if(PLAYER[0].y >= ROWS){
                GAME_OVER = true;
            }else{
                if(BOARD[PLAYER[0].y][PLAYER[0].x] == FOOD){
                    PLAYER.push( { x: PLAYER[PLAYER.length -1].x, y:PLAYER[PLAYER.length -1].y } );
                    createFood();
                }else if(BOARD[PLAYER[0].y][PLAYER[0].x] == SNAKE){
                    GAME_OVER = true;
                }
            }
        }
    }else{
        if(GAME_OVER){
            fill(0, 157, 255);
            textSize(SQUARE_SIZE * 3);
            var t = "You lost!";
            text(t, width/2 - textWidth(t)/2, height/2);
        }
    }
}