---
{
  "projection_kind": "taulib_declaration",
  "title": "root_of_unity_factor_right",
  "permalink": "/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-factor-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Cyclotomic`.",
  "declaration_id": "TauLib.BookI.Boundary.Cyclotomic::root_of_unity_factor_right",
  "declaration_slug": "root-of-unity-factor-right",
  "kind": "theorem",
  "name": "root_of_unity_factor_right",
  "module_name": "TauLib.BookI.Boundary.Cyclotomic",
  "module_url": "/verify/taulib/docs/book-i-boundary-cyclotomic/",
  "source_line_start": 100,
  "source_line_end": 103,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L100-L103",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Cyclotomic",
        "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L100-L103",
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

- Module: [TauLib.BookI.Boundary.Cyclotomic](/verify/taulib/docs/book-i-boundary-cyclotomic/)
- Source path: [`TauLib/BookI/Boundary/Cyclotomic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L100-L103)
- Source range: L100-L103
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Factor right: a root mod m1*m2 is a root mod m2. -/
```

## Source Excerpt

```lean
theorem root_of_unity_factor_right (n : Nat) (z m1 m2 : TauIdx)
    (hz : IsRootOfUnity n z (m1 * m2)) : IsRootOfUnity n z m2 := by
  rw [Nat.mul_comm] at hz
  exact root_of_unity_factor_left n z m2 m1 hz
```
