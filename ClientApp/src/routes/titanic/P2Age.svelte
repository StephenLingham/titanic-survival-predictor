<script>
	import { createForm } from 'felte'

	export let initialValues;
	export let onSubmit;
	export let onBack;
    export let pagesState;

    let selectedAge = 60;

	const { form, data } = createForm({ onSubmit, initialValues })
    console.log(pagesState)
</script>

<form use:form>
	<h2>Age</h2>
    <div style="margin-bottom: 20px">
        {#if pagesState[0].Gender == "true"}
            {#if selectedAge < 3}
            <img src="/male-baby.png" alt="Male Baby" style="border-radius: 120px"/>
        {:else if selectedAge < 18}
            <img src="/male-child.png" alt="Male Child" style="border-radius: 120px"/>
        {:else if selectedAge < 70}
            <img src="/male-adult.png" alt="Male Adult" style="border-radius: 120px"/>
        {:else}
            <img src="/male-elderly.png" alt="Male Elderly" style="border-radius: 120px"/>
        {/if}

        {:else}
            {#if selectedAge < 3}
            <img src="/female-baby.png" alt="Female Baby" style="border-radius: 120px"/>
        {:else if selectedAge < 18}
            <img src="/female-child.png" alt="Female Child" style="border-radius: 120px"/>
        {:else if selectedAge < 70}
            <img src="/female-adult.png" alt="Female Adult" style="border-radius: 120px"/>
        {:else}
            <img src="/female-elderly.png" alt="Feale Elderly" style="border-radius: 120px"/>
        {/if}
    {/if}
    </div>

    <div style="margin-bottom: 20px">
        <!-- <p>0</p> -->
        <input name=selectedAge type=range bind:value={selectedAge} min=0 max=120 style="width:650px;" class="slider">
        <!-- <p>120</p> -->
    </div>
    <div>
        <input name=selectedAge type=number bind:value={selectedAge} min=0 max=120 style="width:90px; text-align: center; font-size: 40px">
    </div>

	<button class="prev" type=button on:click={() => onBack($data)}>Previous page</button>
	<button class="next" type=submit>Next page</button>

</form>

<style>
    .slider {
  -webkit-appearance: none;
  width: 100%;
  height: 25px;
  background: #d3d3d3;
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
}

.slider:hover {
  opacity: 12;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 40px;
  height: 40px;
  background: #1e29cb;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 25px;
  height: 25px;
  background: #04AA6D;
  cursor: pointer;
}
</style>