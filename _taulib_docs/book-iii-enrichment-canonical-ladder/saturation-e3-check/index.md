---
{
  "projection_kind": "taulib_declaration",
  "title": "saturation_e3_check",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/saturation-e3-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::saturation_e3_check",
  "declaration_slug": "saturation-e3-check",
  "kind": "def",
  "name": "saturation_e3_check",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 138,
  "source_line_end": 164,
  "registry_ids": [
    "III.T03"
  ],
  "related_registry_items": [
    {
      "id": "III.T03",
      "title": "Saturation at E₃",
      "url": "/registry/object/III.T03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L138-L164",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.CanonicalLadder",
        "url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L138-L164",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/verify/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L138-L164)
- Source range: L138-L164
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T03` — Saturation at E₃

## Immediate Comment / Docstring

```lean
/-- [III.T03] Saturation at E₃: E₄ = E₃.
    The enrichment ladder saturates at exactly four levels.
    The 4-orbit closure of ρ under ABCD decomposition means
    no fifth orbit exists. -/
```

## Source Excerpt

```lean
def saturation_e3_check (bound db : TauIdx) : Bool :=
  functor_collapse_check bound db &&
  -- Verify: the 4 orbits are exhaustive
  -- At any stage k, ABCD extraction covers all residues
  go 1 ((db + 1))
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      -- Every x in [0, P_k) has an ABCD extraction
      let all_covered := check_coverage k 0 pk (pk + 1)
      all_covered && go (k + 1) (fuel - 1)
  termination_by fuel
  check_coverage (k x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- ABCD extraction: CRT roundtrip via 2 × 3 = 6
      let a_val := x % 2  -- A component (mod 2)
      let rest := x / 2
      let b_val := rest % 3  -- B component (mod 3)
      -- CRT roundtrip: a + 2b reconstructs x mod 6 (exercises Nat.mod, Nat.div)
      let roundtrip := a_val + 2 * b_val == x % 6
      roundtrip && check_coverage k (x + 1) pk (fuel - 1)
  termination_by fuel
```
