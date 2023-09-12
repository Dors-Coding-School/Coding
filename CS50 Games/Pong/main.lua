push = require "push"

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

paddle_speed = 200

function love.load()
    love.graphics.setDefaultFilter('nearest', 'nearest')

    math.randomseed(os.time())

    smallfont = love.graphics.newFont('font.ttf', 12)
    scorefont = love.graphics.newFont('font.ttf', 36)

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        resizable = false,
        vsync = true
    })

    player1Y = 30
    player2Y = VIRTUAL_HEIGHT - 50

    ballX = VIRTUAL_WIDTH / 2 - 2
    ballY = VIRTUAL_HEIGHT / 2 - 2

    ballDX = math.random(2) == 1 and 100 or -100
    ballDY = math.random(-50, 50)

    gameState = 'start'

    player1Score = 0
    player2Score = 0
end

function love.update(dt)
    if love.keyboard.isDown('w') then
        player1Y = math.max(0, player1Y - paddle_speed * dt)
    elseif love.keyboard.isDown('s') then
        player1Y = math.min(VIRTUAL_HEIGHT - 20, player1Y + paddle_speed * dt)
    end

    if love.keyboard.isDown('up') then
        player2Y = math.max(0, player2Y - paddle_speed * dt)
    elseif love.keyboard.isDown('down') then
        player2Y = math.min(VIRTUAL_HEIGHT - 20, player2Y + paddle_speed * dt)
    end

    if gameState == 'play' then
        ballX = ballX + ballDX * dt
        ballY = ballY + ballDY * dt
        if ballX <= 0 then
            player2Score = player2Score + 1
            resetBall()
        elseif ballX >= VIRTUAL_WIDTH - 5 then
            player1Score = player1Score + 1
            resetBall()
        end
    end

    if ballX <= 15 and ballY >= player1Y and ballY <= player1Y + 20 then
        ballDX = math.abs(ballDX)
    end
    
    if ballX >= VIRTUAL_WIDTH - 15 and ballY >= player2Y and ballY <= player2Y + 20 then
        ballDX = -math.abs(ballDX)
    end
    
    if ballY <= 0 or ballY >= VIRTUAL_HEIGHT then
        ballDY = -ballDY
    end
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    elseif key == 'enter' or key == 'return' then
        if gameState == 'start' then
            gameState = 'play'
        else
            gameState = 'start'

            ballX = VIRTUAL_WIDTH / 2 - 2
            ballY = VIRTUAL_HEIGHT / 2 - 2

            ballDX = math.random(2) == 1 and 100 or -100
            ballDY = math.random(-50, 50) * 1.5
        end
    end
end


function love.draw()
    push:apply('start')

    love.graphics.clear(40/255, 50/255, 60/255, 255/255)

    love.graphics.setFont(smallfont)
    if gameState == 'start' then
        love.graphics.printf("Start Pong", 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'play' then
        love.graphics.printf("Play Pong", 0, 20, VIRTUAL_WIDTH, 'center')
    end

    love.graphics.rectangle('fill', 10, player1Y, 5, 20)

    love.graphics.rectangle('fill', VIRTUAL_WIDTH - 10, player2Y, 5, 20)

    love.graphics.rectangle('fill', ballX, ballY, 4, 4)

    love.graphics.setFont(scorefont)
    love.graphics.print(player1Score, VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 4)

    love.graphics.print(player2Score, VIRTUAL_WIDTH / 2 + 20, VIRTUAL_HEIGHT / 4)

    displayFPS()

    push:apply('end')
end

function displayFPS()
    love.graphics.setColor(0, 1, 0, 1)
    love.graphics.setFont(smallfont)
    love.graphics.print('FPS: '.. tostring(love.timer.getFPS()), 40, 20)
end

function resetBall()
    ballX = VIRTUAL_WIDTH / 2 - 2
    ballY = VIRTUAL_HEIGHT / 2 - 2
end
