---
{
  "projection_kind": "taulib_declaration",
  "title": "succ_monotone",
  "permalink": "/verify/taulib/docs/book-iii-hinge-dependency-chain/succ-monotone/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Hinge.DependencyChain`.",
  "declaration_id": "TauLib.BookIII.Hinge.DependencyChain::succ_monotone",
  "declaration_slug": "succ-monotone",
  "kind": "theorem",
  "name": "succ_monotone",
  "module_name": "TauLib.BookIII.Hinge.DependencyChain",
  "module_url": "/verify/taulib/docs/book-iii-hinge-dependency-chain/",
  "source_line_start": 337,
  "source_line_end": 339,
  "registry_ids": [
    "III.P29"
  ],
  "related_registry_items": [
    {
      "id": "III.P29",
      "title": "Chain Verification Protocol",
      "url": "/registry/object/III.P29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L337-L339",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L337-L339",
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
- Source path: [`TauLib/BookIII/Hinge/DependencyChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/DependencyChain.lean#L337-L339)
- Source range: L337-L339
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P29` — Chain Verification Protocol

## Immediate Comment / Docstring

```lean
/-- [III.P29] Structural: successor always increases index (except at E3p). -/
```

## Source Excerpt

```lean
theorem succ_monotone (link : ChainLink) :
    link.toNat <= link.succ.toNat := by
  cases link <;> simp [ChainLink.toNat, ChainLink.succ]
```
