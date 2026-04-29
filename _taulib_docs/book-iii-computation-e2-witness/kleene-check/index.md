---
{
  "projection_kind": "taulib_declaration",
  "title": "kleene_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/kleene-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::kleene_check",
  "declaration_slug": "kleene-check",
  "kind": "def",
  "name": "kleene_check",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 79,
  "source_line_end": 87,
  "registry_ids": [
    "III.D83"
  ],
  "related_registry_items": [
    {
      "id": "III.D83",
      "title": "Kleene Fixed Point",
      "url": "/registry/object/III.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L79-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L79-L87",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L79-L87)
- Source range: L79-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D83` — Kleene Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D83] Kleene check: fixed points exist at every stage. -/
```

## Source Excerpt

```lean
def kleene_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      count_fixed_points k > 0 && go (k + 1) (fuel - 1)
  termination_by fuel
```
