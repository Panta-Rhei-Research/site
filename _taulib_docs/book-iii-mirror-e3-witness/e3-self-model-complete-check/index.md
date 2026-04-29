---
{
  "projection_kind": "taulib_declaration",
  "title": "e3_self_model_complete_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/e3-self-model-complete-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::e3_self_model_complete_check",
  "declaration_slug": "e3-self-model-complete-check",
  "kind": "def",
  "name": "e3_self_model_complete_check",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 154,
  "source_line_end": 173,
  "registry_ids": [
    "III.T58"
  ],
  "related_registry_items": [
    {
      "id": "III.T58",
      "title": "E₃ Self-Model Completeness",
      "url": "/registry/object/III.T58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L154-L173",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L154-L173",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L154-L173)
- Source range: L154-L173
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T58` — E₃ Self-Model Completeness

## Immediate Comment / Docstring

```lean
/-- [III.T58] Self-model completeness: every reduce-stable element
    has the E₃ property (functor E₂→E₃ is surjective on content). -/
```

## Source Excerpt

```lean
def e3_self_model_complete_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      go_x 0 pk k fuel && go (k + 1) (fuel - 1)
  termination_by fuel
  go_x (x pk k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- If x is reduce-stable (E₂ carrier), then x has E₃ property
      let is_e2 := reduce x k == x
      let is_e3 := e3_predicate x k
      let ok := !is_e2 || is_e3
      ok && go_x (x + 1) pk k (fuel - 1)
  termination_by fuel
```
