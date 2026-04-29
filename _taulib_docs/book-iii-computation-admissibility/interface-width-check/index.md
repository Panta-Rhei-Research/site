---
{
  "projection_kind": "taulib_declaration",
  "title": "interface_width_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/interface-width-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::interface_width_check",
  "declaration_slug": "interface-width-check",
  "kind": "def",
  "name": "interface_width_check",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 65,
  "source_line_end": 74,
  "registry_ids": [
    "III.D53"
  ],
  "related_registry_items": [
    {
      "id": "III.D53",
      "title": "Interface Width",
      "url": "/registry/object/III.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L65-L74",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.Admissibility",
        "url": "/verify/taulib/docs/book-iii-computation-admissibility/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L65-L74",
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

- Module: [TauLib.BookIII.Computation.Admissibility](/verify/taulib/docs/book-iii-computation-admissibility/)
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L65-L74)
- Source range: L65-L74
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D53` — Interface Width

## Immediate Comment / Docstring

```lean
/-- [III.D53] Interface width check: all inputs have finite width ≤ db. -/
```

## Source Excerpt

```lean
def interface_width_check (bound db : TauIdx) : Bool :=
  go 0 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let w := interface_width x db
      w <= db && go (x + 1) (fuel - 1)
  termination_by fuel
```
