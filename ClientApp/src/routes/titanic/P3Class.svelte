<script>
	import { createForm } from 'felte'
	
	export let initialValues;
	export let onSubmit;
	export let onBack;

    let passengerClasses = [
		{ id: 1, text: `First class` },
		{ id: 2, text: `Second class` },
		{ id: 3, text: `Third class` }
	];	

	let selectedClass = 3;
    	
	const { form, data } = createForm({ onSubmit, initialValues })

    function upateSelected() {
        selectedClass = selectedClass;
// 		alert(`answered question ${selected.id} (${selected.text}) with "${answer}"`);
	}
</script>

<form use:form>
    <h2>Passenger Class</h2>
    <div style="margin-bottom: 20px">
	<select name=selectedClass bind:value={selectedClass} on:change="{()=> upateSelected()}">
		{#each passengerClasses as pClass}
			<option value={pClass.id}>
				{pClass.text}
			</option>
		{/each}
	</select>
    </div>

	<button class="prev" type=button on:click={() => onBack($data)}>Previous page</button>
	<button class="next" type=submit disabled={!selectedClass}>Submit</button>
</form>

{#if selectedClass == 1}
<img src="PassengerClass1.png" alt="Titanic First Class" style="width:450px; height:450px; border-radius: 15px">
{/if}

{#if selectedClass == 2}
<img src="PassengerClass2.png" alt="Titanic Second Class" style="width:450px; height:450px; border-radius: 15px">
{/if}

{#if selectedClass == 3}
<img src="PassengerClass3.png" alt="Titanic Third Class" style="width:450px; height:450px; border-radius: 15px">
{/if}

<style>
    select{
        font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        width:190px;
        text-align: center; 
        font-size: 25px
    }
</style>