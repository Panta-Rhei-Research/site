---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_complexity_bridge_concrete",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-three-sat/tau-complexity-bridge-concrete/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.ThreeSAT`.",
  "declaration_id": "TauLib.BookIII.Spectrum.ThreeSAT::tau_complexity_bridge_concrete",
  "declaration_slug": "tau-complexity-bridge-concrete",
  "kind": "theorem",
  "name": "tau_complexity_bridge_concrete",
  "module_name": "TauLib.BookIII.Spectrum.ThreeSAT",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-three-sat/",
  "source_line_start": 151,
  "source_line_end": 157,
  "registry_ids": [
    "I.P32"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L151-L157",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.ThreeSAT",
        "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L151-L157",
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

- Module: [TauLib.BookIII.Spectrum.ThreeSAT](/verify/taulib/docs/book-iii-spectrum-three-sat/)
- Source path: [`TauLib/BookIII/Spectrum/ThreeSAT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L151-L157)
- Source range: L151-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.P32] The τ-complexity bridge: the spectral encoding translates
    Boolean satisfiability into a problem about τ-framework values.

    Key structural fact: for concrete CNF formulas, we can verify
    satisfiability by searching over CRT residues. -/
```

## Source Excerpt

```lean
theorem tau_complexity_bridge_concrete :
    ∃ (φ : CNF) (a : Assignment), φ.eval a = true ∧
    ∃ v : TauIdx, spectral_cnf φ v = true := by
  -- Witness: the formula (x₁) with assignment x₁=true
  refine ⟨⟨[⟨⟨1, true⟩, ⟨1, true⟩, ⟨1, true⟩⟩], 1⟩, fun _ => true, ?_, ?_⟩
  · native_decide
  · exact ⟨1, by native_decide⟩
```
