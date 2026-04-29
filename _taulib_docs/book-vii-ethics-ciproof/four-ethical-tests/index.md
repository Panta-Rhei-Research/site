---
{
  "projection_kind": "taulib_declaration",
  "title": "FourEthicalTests",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/four-ethical-tests/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::FourEthicalTests",
  "declaration_slug": "four-ethical-tests",
  "kind": "structure",
  "name": "FourEthicalTests",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 264,
  "source_line_end": 274,
  "registry_ids": [
    "VII.D69"
  ],
  "related_registry_items": [
    {
      "id": "VII.D69",
      "title": "Four Ethical Tests",
      "url": "/registry/object/VII.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L264-L274",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L264-L274",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L264-L274)
- Source range: L264-L274
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D69` — Four Ethical Tests

## Immediate Comment / Docstring

```lean
/-- [VII.D69] Four Ethical Tests (ch82). Maxim M admissible iff all pass:
    (1) Universalizability: ω(M) = 0 (vanishing Čech obstruction)
    (2) Respect: D(M(X)) ≅ D(X) for all affected agents
    (3) Coherence: global section compatible with duty portfolio
    (4) Monodromy: Hol_M(γ) = Id for all relevant loops -/
```

## Source Excerpt

```lean
structure FourEthicalTests where
  /-- (1) Universalizability. -/
  universalizable : Bool := true
  /-- (2) Respect (dignity preservation). -/
  respect : Bool := true
  /-- (3) Coherence. -/
  coherent : Bool := true
  /-- (4) Monodromy-free. -/
  monodromy_free : Bool := true
  test_count : Nat := 4
  deriving Repr
```
