---
{
  "projection_kind": "taulib_declaration",
  "title": "no_forced_stance",
  "permalink": "/verify/taulib/docs/book-vii-final-boundary/no-forced-stance/",
  "summary_short": "`def` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::no_forced_stance",
  "declaration_slug": "no-forced-stance",
  "kind": "def",
  "name": "no_forced_stance",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/verify/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 216,
  "source_line_end": 222,
  "registry_ids": [
    "VII.T47"
  ],
  "related_registry_items": [
    {
      "id": "VII.T47",
      "title": "No Forced Stance",
      "url": "/registry/object/VII.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L216-L222",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Final.Boundary",
        "url": "/verify/taulib/docs/book-vii-final-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L216-L222",
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

- Module: [TauLib.BookVII.Final.Boundary](/verify/taulib/docs/book-vii-final-boundary/)
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L216-L222)
- Source range: L216-L222
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VII.T47` — No Forced Stance

## Immediate Comment / Docstring

```lean
/-- [VII.T47] No-Forced-Stance commitment.

    Retired from `theorem no_forced_stance : True := sorry`
    in peer-review-fixes-v1 (2026-04-19). Pre-publication peer
    review identified the `True := sorry` encoding as performative
    (True is provable by `trivial`) and self-referential (the
    surrounding docstring cited VII.T47 to justify leaving VII.T47
    as a sorry — which IS this declaration).

    The commitment is now data, not an unproven proposition.
    A reader can `#eval no_forced_stance.statement` to inspect
    what is being committed to and `#eval no_forced_stance.warrant`
    to inspect why. `#print axioms no_forced_stance` reports no
    axioms (it is a `def`). -/
```

## Source Excerpt

```lean
def no_forced_stance : Commitment :=
  { statement := "The structural framework does not force a stance here"
    warrant := "Constitutive of the framework; see Book VII ch. 123 — " ++
               "proving this would require the very standpoint it denies"
    registry_id := "VII.T47" }

end Tau.BookVII.Final.Boundary
```
