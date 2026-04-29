---
{
  "projection_kind": "taulib_declaration",
  "title": "stage_zero_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-cylinders/stage-zero-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Cylinders`.",
  "declaration_id": "TauLib.BookII.Domains.Cylinders::stage_zero_check",
  "declaration_slug": "stage-zero-check",
  "kind": "def",
  "name": "stage_zero_check",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_url": "/verify/taulib/docs/book-ii-domains-cylinders/",
  "source_line_start": 100,
  "source_line_end": 107,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L100-L107",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Cylinders",
        "url": "/verify/taulib/docs/book-ii-domains-cylinders/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L100-L107",
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

- Module: [TauLib.BookII.Domains.Cylinders](/verify/taulib/docs/book-ii-domains-cylinders/)
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L100-L107)
- Source range: L100-L107
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T04, clause 2] Stage 0: C_0(x) = everything.
    primorial 0 = 1, so reduce y 0 = 0 for all y. -/
```

## Source Excerpt

```lean
def stage_zero_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if y > bound then true
    else cylinder_mem 0 0 y && go (y + 1) (fuel - 1)
  termination_by fuel
```
