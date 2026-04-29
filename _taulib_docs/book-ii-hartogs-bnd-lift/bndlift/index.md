---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/bndlift/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::bndlift",
  "declaration_slug": "bndlift",
  "kind": "def",
  "name": "bndlift",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 118,
  "source_line_end": 119,
  "registry_ids": [
    "II.D36"
  ],
  "related_registry_items": [
    {
      "id": "II.D36",
      "title": "BndLift Construction",
      "url": "/registry/object/II.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L118-L119",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L118-L119",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L118-L119)
- Source range: L118-L119
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D36` — BndLift Construction

## Immediate Comment / Docstring

```lean
/-- [II.D36] BndLift: promote stage-n data to stage-(n+1) data.

    At the TauIdx level, the lift of x to stage (n+1) is simply
    reduce(x, n+1): we read off the residue modulo P_{n+1}.

    This is the key observation: the BndLift construction at the
    level of the inverse system IS the reduction map, viewed from
    one stage higher. The new information at stage n+1 is the
    residue mod p_{n+1}, which CRT decomposes into a separate
    independent coordinate. -/
```

## Source Excerpt

```lean
def bndlift (x : TauIdx) (stage : TauIdx) : TauIdx :=
  reduce x (stage + 1)
```
