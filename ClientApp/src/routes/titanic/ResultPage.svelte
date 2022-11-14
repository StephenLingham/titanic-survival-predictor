<script>
    export let result;
    export let result2;

    export let onRestart;
    if (result == 0)
              {
                result = "You died"
              }
            if(result == 1)
              {
                result = "You Survived"
              }
</script>

<button class="next" type=button on:click={() => onRestart()}>Start again</button>

<p>{result}</p>
<p>You had a {Math.round(result2, 2)}% chance of Survival</p>

{#if result == "You Survived"}
<img src="Survived.jpg" alt="Survived" style="width:450px; height:450px; border-radius: 15px">
{/if}

{#if result == "You died"}
<img src="Dead.gif" alt="Dead" style="width:450px; height:450px; border-radius: 15px">
{/if}
