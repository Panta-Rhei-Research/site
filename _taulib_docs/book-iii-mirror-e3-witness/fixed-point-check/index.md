---
{
  "projection_kind": "taulib_declaration",
  "title": "fixed_point_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/fixed-point-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::fixed_point_check",
  "declaration_slug": "fixed-point-check",
  "kind": "def",
  "name": "fixed_point_check",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 83,
  "source_line_end": 91,
  "registry_ids": [
    "III.D85"
  ],
  "related_registry_items": [
    {
      "id": "III.D85",
      "title": "Self-Referential Fixed Point",
      "url": "/registry/object/III.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L83-L91",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L83-L91",
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
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L83-L91)
- Source range: L83-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D85` — Self-Referential Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D85] Fixed point check: E₃ fixed points exist at every stage. -/
```

## Source Excerpt

```lean
def fixed_point_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      count_e3_fixed_points k > 0 && go (k + 1) (fuel - 1)
  termination_by fuel
```
