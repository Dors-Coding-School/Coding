ScoreState = Class{__includes = BaseState}

local cooper = love.graphics.newImage('cooper.png')
local silver = love.graphics.newImage('silver.png')
local gold = love.graphics.newImage('gold.png')

function ScoreState:enter(params)
    self.score = params.score
end

function ScoreState:update(dt)
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        gStateMachine:change('countdown')
    end
end

function ScoreState:render()
    if self.score >= 0 and self.score < 10 then
        love.graphics.draw(cooper, 55, -10, 0, 400/cooper:getWidth(), 300/cooper:getHeight())
        love.graphics.setFont(flappyFont)
        love.graphics.printf('Bronze!', 0, 64, VIRTUAL_WIDTH, 'center')
    end
    if self.score >= 10 and self.score < 20 then
        love.graphics.draw(silver, 55, -10, 0, 400/cooper:getWidth(), 300/cooper:getHeight())
        love.graphics.setFont(flappyFont)
        love.graphics.printf('Silver!', 0, 64, VIRTUAL_WIDTH, 'center')
    end
    if self.score >= 20 then
        love.graphics.draw(gold, 55, -10, 0, 400/cooper:getWidth(), 300/cooper:getHeight())
        love.graphics.setFont(flappyFont)
        love.graphics.printf('Gold!!!!', 0, 64, VIRTUAL_WIDTH, 'center')
    end

    love.graphics.setFont(mediumFont)
    love.graphics.printf('Score: ' .. tostring(self.score), 0, 110, VIRTUAL_WIDTH, 'center')

    love.graphics.printf('Press Enter to Play Again!', 0, 160, VIRTUAL_WIDTH, 'center')
end