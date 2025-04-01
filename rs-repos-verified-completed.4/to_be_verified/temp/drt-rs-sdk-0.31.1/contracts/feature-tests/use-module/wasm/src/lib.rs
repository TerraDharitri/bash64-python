////////////////////////////////////////////////////
////////////////// AUTO-GENERATED //////////////////
////////////////////////////////////////////////////

#![no_std]

numbat_wasm_node::wasm_endpoints! {
    use_module
    (
        callBack
        call_derived_not_owner_only
        call_mod_a
        call_mod_b
        call_mod_c
        cancel
        changeLockTimeAfterVotingEndsInBlocks
        changeMinTokenBalanceForProposing
        changeQuorum
        changeVotingDelayInBlocks
        changeVotingPeriodInBlocks
        checkFeatureGuard
        checkPause
        depositTokensForAction
        dnsRegister
        downvote
        execute
        getGovernanceTokenId
        getLockTimeAfterVotingEndsInBlocks
        getMinTokenBalanceForProposing
        getProposalActions
        getProposalDescription
        getProposalStatus
        getProposer
        getQuorum
        getTotalDownvotes
        getTotalVotes
        getVotingDelayInBlocks
        getVotingPeriodInBlocks
        initGovernanceModule
        isPaused
        issueToken
        only_owner_mod_endpoint
        pause
        propose
        queue
        setFeatureFlag
        unpause
        vote
        withdrawGovernanceTokens
    )
}
