---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L314",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/example-l314/",
  "summary_short": "`example` declaration in `TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR::#eval:314",
  "declaration_slug": "example-l314",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/",
  "source_line_start": 314,
  "source_line_end": 320,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L314-L320",
  "formal_status": "example",
  "declaration_role": "example check",
  "formal_status_label": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR",
        "url": "/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L314-L320",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "role": "example check",
      "status": "example"
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

- Module: [TauLib.BookI.Holomorphy.H6EarnedCodomainWaveCR](/corpus/taulib/docs/book-i-holomorphy-h6-earned-codomain-wave-cr/)
- Source path: [`TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6EarnedCodomainWaveCR.lean#L314-L320)
- Source range: L314-L320
- Kind: `example`
- Public role: `example check`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A concrete example of operator commutativity: shift-by-1 and
    shift-by-2 commute as operators on `ℤ → ℤ`.

    The key fact for the wave equation: any two shift operators
    commute (translation operators always commute). -/
```

## Source Excerpt

```lean
example (f : Int → Int) :
    (fun n => f (n + 2 + 1)) = (fun n => f (n + 1 + 2)) := by
  funext n
  congr 1
  ring

end Tau.Holomorphy
```
