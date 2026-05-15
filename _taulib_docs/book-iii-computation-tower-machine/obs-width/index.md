---
{
  "projection_kind": "taulib_declaration",
  "title": "obs_width",
  "permalink": "/corpus/taulib/docs/book-iii-computation-tower-machine/obs-width/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::obs_width",
  "declaration_slug": "obs-width",
  "kind": "theorem",
  "name": "obs_width",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/corpus/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 209,
  "source_line_end": 211,
  "registry_ids": [
    "III.D52"
  ],
  "related_registry_items": [
    {
      "id": "III.D52",
      "title": "Observable Transition",
      "url": "/registry/object/III.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L209-L211",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.TowerMachine",
        "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L209-L211",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Computation.TowerMachine](/corpus/taulib/docs/book-iii-computation-tower-machine/)
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L209-L211)
- Source range: L209-L211
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D52` — Observable Transition

## Immediate Comment / Docstring

```lean
/-- [III.D52] Structural: observable width is 3. -/
```

## Source Excerpt

```lean
theorem obs_width : observable_width = 3 := rfl

end Tau.BookIII.Computation
```
