local function GetAllClothesTable()
    local clothesCategory = {
        [0] = "HEAD",
        [1] = "BERD",
        [2] = "HAIR",
        [3] = "UPPR",
        [4] = "LOWR",
        [5] = "HAND",
        [6] = "FEET",
        [7] = "TEEF",
        [8] = "ACCS",
        [9] = "TASK",
        [10] = "DECL",
        [11] = "JBIB"
    }
    local clothesTable = {}
    local playerPed = PlayerPedId()
    for i, category in pairs(clothesCategory) do
        local drawableVariation = GetPedDrawableVariation(playerPed, i)
        local textureVariation = GetPedTextureVariation(playerPed, i)
        local numberOfTextures = GetNumberOfPedTextureVariations(playerPed, i, drawableVariation)

        clothesTable[category] = {
            objID = drawableVariation,
            txtID = textureVariation,
            objTotalTxt = numberOfTextures
        }
    end

    return clothesTable
end


local function SetNui(bool)
    SetNuiFocus(bool, bool)
end

RegisterCommand('umsoup', function()
    SetNui(true)
    SendNUIMessage({
        clothesData = GetAllClothesTable()
    })
end, false)

RegisterNuiCallback('close', function(_, cb)
    SetNui(false)
    cb(1)
end)
