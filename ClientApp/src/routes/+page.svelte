<script>
	import StartPage from "./titanic/StartPage.svelte";
	import Stats from "./titanic/Stats.svelte";
	import UserStats from "./titanic/UserStats.svelte";

	let gameStarted = 0;
	let showStats = 0;
	let showHome = 1;

	function onPlay(){
		showHome = 0;
		showStats = 0;
		gameStarted = 1;
	}

	function onShowStats(){
		showHome = 0;
		gameStarted = 0;
		showStats = 1;
	}

	function onHome(){
		showHome = 1;
		showStats = 0;
		gameStarted = 0;
	}
</script>

<section>
	<button class="home" type=button on:click={() => onHome()}>
		<img src="/homeIcon.png" width="30px" height= "30px" alt="Home">
	</button>

	{#if gameStarted === 0 && showHome === 1}
		<h1>Titanic Survival Game</h1>

		<h2>Would you have survived in the Titanic?</h2>

        <div>
            <button class="play" type=button on:click={() => onPlay()}>Play!</button>
        </div>
		<button class="play" type=button on:click={() => onShowStats()}>Show Stats</button>
	{/if}

	{#if gameStarted === 1}
		<StartPage />
	{/if}

	{#if showStats === 1}
		<UserStats/>
		<Stats/>
	{/if}

</section>

<style global>
	body{
		font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
		font-size: 24px;
		background-image: url("/SinkingShip.png");	
		background-repeat: no-repeat;
		background-size: cover;
		background-color: black;
	}

	h1{
		font-size: 45px;
	}

	h2{
		font-size: 30px;
	}

	section{
		border-radius: 25px;
		background-color: rgba(255, 255, 255, 0.6);
		text-align: center;
		width: 60%;
		margin: 0 auto;
		height: 600px;
		padding: 5%;
		position: relative;
	}	

	button {
		background: #1366d6;
		border-radius: 999px;
		box-shadow: #1366d6 0 10px 20px -10px;
		box-sizing: border-box;
		color: #FFFFFF;
		cursor: pointer;
		font-family: Inter,Helvetica,"Apple Color Emoji","Segoe UI Emoji",NotoColorEmoji,"Noto Color Emoji","Segoe UI Symbol","Android Emoji",EmojiSymbols,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans",sans-serif;
		font-size: 16px;
		font-weight: 700;
		line-height: 24px;
		opacity: 1;
		outline: 0 solid transparent;
		padding: 8px 18px;
		user-select: none;
		-webkit-user-select: none;
		touch-action: manipulation;
		width: fit-content;
		word-break: break-word;
		border: 0;
	}

	button:hover {
		transform: translateY(-2px);
	}
	
	button.next{
		position: absolute;
		bottom: 25px;
		right: 25px;
	}

	button.prev{
		position: absolute;
		bottom: 25px;
		left: 25px;
	}

	button.play{
		margin-top: 50px;
		font-size: 50px;
		padding: 30px;
	}
	
	button.home{
		position: absolute;
		top: 25px;
		left: 25px;
	}
</style>