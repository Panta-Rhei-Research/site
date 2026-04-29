---
{
  "projection_kind": "taulib_declaration",
  "title": "norm_definiteness_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/norm-definiteness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::norm_definiteness_check",
  "declaration_slug": "norm-definiteness-check",
  "kind": "def",
  "name": "norm_definiteness_check",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 97,
  "source_line_end": 99,
  "registry_ids": [
    "II.D83"
  ],
  "related_registry_items": [
    {
      "id": "II.D83",
      "title": "L² Norm",
      "url": "/registry/object/II.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L97-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L97-L99",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L97-L99)
- Source range: L97-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D83` — L² Norm

## Immediate Comment / Docstring

```lean
/-- [II.D83] Definiteness check: ‖f‖² = 0 implies f = 0 (on support). -/
```

## Source Excerpt

```lean
def norm_definiteness_check (k : Nat) : Bool :=
  let zero_fn : Nat → Int := fun _ => 0
  l2_norm_sq zero_fn k == 0
```
