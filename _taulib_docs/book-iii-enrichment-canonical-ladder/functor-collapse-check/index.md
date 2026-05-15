---
{
  "projection_kind": "taulib_declaration",
  "title": "functor_collapse_check",
  "permalink": "/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/functor-collapse-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::functor_collapse_check",
  "declaration_slug": "functor-collapse-check",
  "kind": "def",
  "name": "functor_collapse_check",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 117,
  "source_line_end": 132,
  "registry_ids": [
    "III.P02",
    "III.T03"
  ],
  "related_registry_items": [
    {
      "id": "III.P02",
      "title": "Functor Category Collapse",
      "url": "/registry/object/III.P02/"
    },
    {
      "id": "III.T03",
      "title": "Saturation at E₃",
      "url": "/registry/object/III.T03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L117-L132",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.CanonicalLadder",
        "url": "/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L117-L132",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/corpus/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L117-L132)
- Source range: L117-L132
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.P02` — Functor Category Collapse
- `III.T03` — Saturation at E₃

## Immediate Comment / Docstring

```lean
/-- [III.P02] Functor category collapse: [E₃^op, E₃] ⊆ E₃.
    The functor category at E₃ does not escape E₃ because:
    1. There are only 4 orbits under ABCD decomposition
    2. The ω-absorber prevents new generators
    3. E₃.succ = E₃ (definitional saturation)

    Computationally: applying the enrichment functor at E₃ yields
    the same layer template (verified by saturation_checker). -/
```

## Source Excerpt

```lean
def functor_collapse_check (bound db : TauIdx) : Bool :=
  -- E₃.succ = E₃ is definitional, so layers are identical
  saturation_checker bound db &&
  -- Additionally verify: the enrichment functor at E₂→E₃ is the last
  -- genuine enrichment step
  enrichment_functor_check .E2 bound db

-- ============================================================
-- SATURATION AT E₃ [III.T03]
-- ============================================================

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
