---
{
  "projection_kind": "taulib_declaration",
  "title": "batch_verify",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau-admissible/batch-verify/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.TauAdmissible`.",
  "declaration_id": "TauLib.BookII.Interior.TauAdmissible::batch_verify",
  "declaration_slug": "batch-verify",
  "kind": "def",
  "name": "batch_verify",
  "module_name": "TauLib.BookII.Interior.TauAdmissible",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau-admissible/",
  "source_line_start": 121,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L121-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L121-L128",
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
- Source path: [`TauLib/BookII/Interior/TauAdmissible.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L121-L128)
- Source range: L121-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T01, clause 1] Batch verification for X = 2..bound. -/
```

## Source Excerpt

```lean
def batch_verify (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (start fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if start > bound then true
    else round_trip_check start && admissible_check start && go (start + 1) (fuel - 1)
  termination_by fuel
```
