"""Execute the frozen Step 2.6 synthetic collision suite v0.1.

This evaluator is subordinate to:
- perception/CURRENT_TRANSITION_SURFACE_V0.1.md
- perception/SYNTHETIC_WORLD_FAMILY_V0.1.md

It performs no network access and grants no source, observation, evidence, claim,
or semantic authority. It only exhausts the already-frozen finite synthetic family.
"""

from itertools import combinations, product

BASE_RHO = (
    "SYNTHETIC_ANCHOR_A0",          # q
    "SYNTHETIC_ANCHOR_A0",          # sigma_id
    "IDENTITY_ONLY",                # extent
    "RESOLVED",                     # outcome
    "LIVE_DIRECT",                  # provenance
    "SINGLE_ATTEMPT_SUCCESS",       # history
)

CONTROL_MUTATIONS = (
    ("C1_TARGET_BINDING", 0, "SYNTHETIC_ANCHOR_B0"),
    ("C2_REALIZED_IDENTITY", 1, "SYNTHETIC_ANCHOR_B0"),
    ("C3_EXTENT", 2, "BOUNDED_PARTIAL_SURFACE"),
    ("C4_OUTCOME", 3, "NOT_RESOLVED"),
    ("C5_PROVENANCE", 4, "STALE_CACHE_SUBSTITUTION_EXPOSED"),
    ("C6_HISTORY", 5, "FAILED_THEN_RESOLVED"),
)


def build_worlds():
    worlds = []

    # Frozen 2^6 latent-property family. Hidden bits are intentionally absent
    # from the current encounter representation.
    for bits in product((0, 1), repeat=6):
        worlds.append(
            {
                "name": "L" + "".join(str(bit) for bit in bits),
                "kind": "latent",
                "hidden": bits,
                "rho": BASE_RHO,
            }
        )

    # Frozen encoder positive controls: each changes exactly one represented
    # coordinate and therefore must fail the equal-representation filter.
    for name, index, value in CONTROL_MUTATIONS:
        rho = list(BASE_RHO)
        rho[index] = value
        worlds.append(
            {
                "name": name,
                "kind": "control",
                "hidden": None,
                "rho": tuple(rho),
            }
        )

    return worlds


def delta_enc_disposition(world):
    """Disposition for the frozen DELTA_ENC oracle on suite candidates.

    Only equal-representation pairs reach this function. Under the frozen
    family, that means latent worlds with the same truthful, resolution-only,
    P1-P4-conforming encounter record. The six hidden axes are outside the
    constituted encounter and cannot alter DELTA_ENC without smuggling a new
    consequence into the oracle.
    """

    if world["rho"] != BASE_RHO:
        raise AssertionError("positive controls must be filtered before oracle evaluation")

    q, sigma_id, extent, outcome, provenance, history = world["rho"]

    if q != sigma_id:
        return "REJECT"
    if extent != "IDENTITY_ONLY":
        return "REJECT"
    if outcome != "RESOLVED":
        return "REJECT"
    if provenance != "LIVE_DIRECT":
        return "REJECT"
    if history != "SINGLE_ATTEMPT_SUCCESS":
        return "REJECT"

    return "ADMIT"


def run():
    worlds = build_worlds()
    pairs = list(combinations(worlds, 2))
    equal_representation_pairs = [
        (left, right)
        for left, right in pairs
        if left["rho"] == right["rho"]
    ]

    # Frozen-suite integrity checks.
    assert len(worlds) == 70
    assert len([world for world in worlds if world["kind"] == "latent"]) == 64
    assert len([world for world in worlds if world["kind"] == "control"]) == 6
    assert len(pairs) == 2415
    assert len(equal_representation_pairs) == 2016
    assert all(
        left["kind"] == "latent" and right["kind"] == "latent"
        for left, right in equal_representation_pairs
    )

    collisions = []
    for left, right in equal_representation_pairs:
        left_disposition = delta_enc_disposition(left)
        right_disposition = delta_enc_disposition(right)
        if left_disposition != right_disposition:
            collisions.append(
                (
                    left["name"],
                    right["name"],
                    left_disposition,
                    right_disposition,
                )
            )

    print("STEP_2_6_SYNTHETIC_WORLD_COUNT=70")
    print("STEP_2_6_TOTAL_UNORDERED_PAIRS=2415")
    print("STEP_2_6_EQUAL_REPRESENTATION_PAIRS=2016")
    print(f"STEP_2_6_COLLISIONS={len(collisions)}")
    print(
        "STEP_2_6_RESULT="
        + (
            "COLLISION_FOUND"
            if collisions
            else "NO_COLLISION_ON_FROZEN_SYNTHETIC_SUITE"
        )
    )

    return 1 if collisions else 0


if __name__ == "__main__":
    raise SystemExit(run())
