---
{
  "projection_kind": "taulib_declaration",
  "title": "seven_plus_seven",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/seven-plus-seven/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::seven_plus_seven",
  "declaration_slug": "seven-plus-seven",
  "kind": "theorem",
  "name": "seven_plus_seven",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 353,
  "source_line_end": 356,
  "registry_ids": [
    "III.D66"
  ],
  "related_registry_items": [
    {
      "id": "III.D66",
      "title": "Complete Dependency Chain",
      "url": "/registry/object/III.D66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L353-L356",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.DependencyChain",
        "url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L353-L356",
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

- Module: [TauLib.BookIII.Hinge.DependencyChain](/verify/taulib/docs/book-iii-hinge-dependency-chain/)
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L353-L356)
- Source range: L353-L356
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D66` — Complete Dependency Chain

## Immediate Comment / Docstring

```lean
/-- [III.D66] Structural: the chain covers 7 axiom links + 7 enrichment links. -/
```

## Source Excerpt

```lean
theorem seven_plus_seven :
    (chain_links.filter (fun l => l.toNat < 7)).length = 7 := by native_decide

end Tau.BookIII.Hinge
```
