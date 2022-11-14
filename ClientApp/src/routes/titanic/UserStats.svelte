<script>
    import axios from 'axios';
    import { onMount } from 'svelte';
    
    let userStats;
    
    async function getUserStats () {
        let response = await axios.get('http://localhost:5000/api/stats')

        return response.data;
	}

    onMount(async () => {
		userStats = await getUserStats();
	});
</script>


<p>Total number of players: {#if userStats !== undefined} {userStats.totalNumberOfUsers} {/if}</p>
<p>Number of players who survived: {#if userStats !== undefined} {userStats.numberOfUsersWhoSurvived} {/if}</p>

