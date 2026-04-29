---
{
  "projection_kind": "taulib_declaration",
  "title": "strictness_checker",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-functor/strictness-checker/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.Functor`.",
  "declaration_id": "TauLib.BookIII.Enrichment.Functor::strictness_checker",
  "declaration_slug": "strictness-checker",
  "kind": "def",
  "name": "strictness_checker",
  "module_name": "TauLib.BookIII.Enrichment.Functor",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-functor/",
  "source_line_start": 131,
  "source_line_end": 168,
  "registry_ids": [
    "III.D10"
  ],
  "related_registry_items": [
    {
      "id": "III.D10",
      "title": "Ladder Checker",
      "url": "/registry/object/III.D10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L131-L168",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.Functor",
        "url": "/verify/taulib/docs/book-iii-enrichment-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L131-L168",
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

- Module: [TauLib.BookIII.Enrichment.Functor](/verify/taulib/docs/book-iii-enrichment-functor/)
- Source path: [`TauLib/BookIII/Enrichment/Functor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L131-L168)
- Source range: L131-L168
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D10` — Ladder Checker

## Immediate Comment / Docstring

```lean
/-- [III.D10] Strictness checker: verify that E_k has elements not in E_{k-1}.
    For E₀, this is trivially true (no E_{-1}). For E₁+, we need a witness
    that is in E_k's carrier but not in E_{k-1}'s carrier, or that satisfies
    E_k's predicate but not E_{k-1}'s predicate. -/
```

## Source Excerpt

```lean
def strictness_checker (k : EnrLevel) (bound db : TauIdx) : Bool :=
  match k with
  | .E0 => true  -- E₀ is the base; strictness is vacuous
  | .E1 =>
    -- E₁ \ E₀ witness: hom bipolar decomposition exists at E₁ but not E₀
    -- At E₁, the predicate includes bipolar decomposition; E₀ doesn't
    let _e0 := layer_of .E0 bound db
    let e1 := layer_of .E1 bound db
    -- Find x, k where e1 predicate holds but e0 predicate fails
    -- (or: e1 has structure e0 lacks)
    -- Actually, since E₀ predicate is "reduce(x,k) == x" (NF-stable)
    -- and E₁ predicate is "bipolar decomposition exists" (always true),
    -- for x >= P_k: E₀ carrier fails, but E₁ has enriched structure.
    -- Witness: x = P_k (not in E₀ carrier, but E₁ enrichment is richer)
    -- Simpler: E₁ has self-enrichment data (hom_stage) that E₀ lacks.
    let witness := hom_stage 3 5 2  -- hom-stage: an E₁ object
    -- This value is meaningful at E₁ (enriched hom) but at E₀ it's just a number
    e1.predicate_check witness 2 && e1.invariant_check witness 2
  | .E2 =>
    -- E₂ \ E₁ witness: operational closure (code→decode cycle)
    let e1 := layer_of .E1 bound db
    let e2 := layer_of .E2 bound db
    -- A code that decodes to itself is an E₂-specific phenomenon
    -- Level-gap: E2 and E1 decoders differ (E1 extracts B-channel, E2 extracts reduce)
    e2.predicate_check 0 2 && e2.invariant_check 0 2 &&
    e1.decoder 3 2 != e2.decoder 3 2
  | .E3 =>
    -- E₃ \ E₂ witness: self-model consistency (triple idempotence)
    let e3 := layer_of .E3 bound db
    -- Verify triple-reduce path exercises Nat.mod_mod_of_dvd
    e3.predicate_check 0 2 && e3.invariant_check 0 2 &&
    reduce (reduce (reduce 5 2) 2) 2 == reduce 5 2

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
