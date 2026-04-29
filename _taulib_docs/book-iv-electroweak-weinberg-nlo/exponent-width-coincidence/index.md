---
{
  "projection_kind": "taulib_declaration",
  "title": "exponent_width_coincidence",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/exponent-width-coincidence/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::exponent_width_coincidence",
  "declaration_slug": "exponent-width-coincidence",
  "kind": "theorem",
  "name": "exponent_width_coincidence",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 85,
  "source_line_end": 88,
  "registry_ids": [
    "IV.P180"
  ],
  "related_registry_items": [
    {
      "id": "IV.P180",
      "title": "Exponent-Width Coincidence",
      "url": "/registry/object/IV.P180/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L85-L88",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L85-L88",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L85-L88)
- Source range: L85-L88
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P180` — Exponent-Width Coincidence

## Immediate Comment / Docstring

```lean
/-- [IV.P180] The NLO exponent 3 has a triple identification:
    1. a₄ = 3 (CF partial quotient)
    2. dim(τ³) = 3 (geometric dimension — base 1 + fiber 2)
    3. W₃ window width = 3 (the algebra itself)
    4. |{π, γ, η}| = 3 (solenoidal cardinality)
    All four are the same number. -/
```

## Source Excerpt

```lean
theorem exponent_width_coincidence :
    weinbergNLO.nlo_exp = 3 ∧
    solenoidalGenerators.length = 3 := by
  exact ⟨rfl, rfl⟩
```
