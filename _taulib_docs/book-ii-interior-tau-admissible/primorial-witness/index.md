---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_witness",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau-admissible/primorial-witness/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.TauAdmissible`.",
  "declaration_id": "TauLib.BookII.Interior.TauAdmissible::primorial_witness",
  "declaration_slug": "primorial-witness",
  "kind": "def",
  "name": "primorial_witness",
  "module_name": "TauLib.BookII.Interior.TauAdmissible",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau-admissible/",
  "source_line_start": 135,
  "source_line_end": 141,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L135-L141",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.TauAdmissible",
        "url": "/verify/taulib/docs/book-ii-interior-tau-admissible/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L135-L141",
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

- Module: [TauLib.BookII.Interior.TauAdmissible](/verify/taulib/docs/book-ii-interior-tau-admissible/)
- Source path: [`TauLib/BookII/Interior/TauAdmissible.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L135-L141)
- Source range: L135-L141
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Primorial P_k = p₁ · p₂ · ... · p_k. -/
```

## Source Excerpt

```lean
def primorial_witness : List (TauIdx × TauAdmissiblePoint) :=
  [ (2,    from_tau_idx 2)      -- P₁ = 2:    Φ = (2,1,1,1)
  , (6,    from_tau_idx 6)      -- P₂ = 6:    Φ = (3,1,1,2)
  , (30,   from_tau_idx 30)     -- P₃ = 30:   Φ = (5,1,1,6)
  , (210,  from_tau_idx 210)    -- P₄ = 210:  Φ = (7,1,1,30)
  , (2310, from_tau_idx 2310)   -- P₅ = 2310: Φ = (11,1,1,210)
  ]
```
