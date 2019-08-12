import GameScene from '../Scenes/GameScene';

class GameRegistry {
    scene:GameScene = new GameScene;
    
	private static instance: GameRegistry;
    constructor() {
		if (GameRegistry.instance) {return GameRegistry.instance;}GameRegistry.instance = this;
    }

}

export default GameRegistry;