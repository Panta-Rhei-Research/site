---
{
  "projection_kind": "taulib_declaration",
  "title": "md_cycle_42_3",
  "permalink": "/verify/taulib/docs/book-iii-doors-mutual-determination/md-cycle-42-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.MutualDetermination`.",
  "declaration_id": "TauLib.BookIII.Doors.MutualDetermination::md_cycle_42_3",
  "declaration_slug": "md-cycle-42-3",
  "kind": "theorem",
  "name": "md_cycle_42_3",
  "module_name": "TauLib.BookIII.Doors.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-iii-doors-mutual-determination/",
  "source_line_start": 142,
  "source_line_end": 149,
  "registry_ids": [
    "III.D25"
  ],
  "related_registry_items": [
    {
      "id": "III.D25",
      "title": "Mutual Determination Schema",
      "url": "/registry/object/III.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L142-L149",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.MutualDetermination",
        "url": "/verify/taulib/docs/book-iii-doors-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L142-L149",
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

- Module: [TauLib.BookIII.Doors.MutualDetermination](/verify/taulib/docs/book-iii-doors-mutual-determination/)
- Source path: [`TauLib/BookIII/Doors/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MutualDetermination.lean#L142-L149)
- Source range: L142-L149
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D25` — Mutual Determination Schema

## Immediate Comment / Docstring

```lean
/-- [III.D25] Structural: mutual determination cycle for 42 at depth 3. -/
```

## Source Excerpt

```lean
theorem md_cycle_42_3 :
    let residues := crt_decompose 42 3
    let reconstructed := crt_reconstruct residues 3
    let nf := boundary_normal_form reconstructed 3
    (nf.b_part + nf.c_part + nf.x_part) % primorial 3 = 42 % primorial 3 := by
  native_decide

end Tau.BookIII.Doors
```
