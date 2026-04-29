---
{
  "projection_kind": "taulib_declaration",
  "title": "den_cauchy_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/den-cauchy-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.OrthodoxBridge`.",
  "declaration_id": "TauLib.BookII.Geometry.OrthodoxBridge::den_cauchy_check",
  "declaration_slug": "den-cauchy-check",
  "kind": "def",
  "name": "den_cauchy_check",
  "module_name": "TauLib.BookII.Geometry.OrthodoxBridge",
  "module_url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/",
  "source_line_start": 89,
  "source_line_end": 97,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L89-L97",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.OrthodoxBridge",
        "url": "/verify/taulib/docs/book-ii-geometry-orthodox-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L89-L97",
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

- Module: [TauLib.BookII.Geometry.OrthodoxBridge](/verify/taulib/docs/book-ii-geometry-orthodox-bridge/)
- Source path: [`TauLib/BookII/Geometry/OrthodoxBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/OrthodoxBridge.lean#L89-L97)
- Source range: L89-L97
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Cauchy property: for all x in [2, bound] and k₂ > k₁,
    reduce(reduce(x, k₂), k₁) = reduce(x, k₁).
    This is the inverse system compatibility from ModArith. -/
```

## Source Excerpt

```lean
def den_cauchy_check (bound stages : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      cauchy_check_k1 x stages && go (x + 1) (fuel - 1)
  termination_by fuel
```
