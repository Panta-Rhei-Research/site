---
{
  "projection_kind": "taulib_declaration",
  "title": "pmns_mixing_angles",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/pmns-mixing-angles/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::pmns_mixing_angles",
  "declaration_slug": "pmns-mixing-angles",
  "kind": "def",
  "name": "pmns_mixing_angles",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 538,
  "source_line_end": 541,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L538-L541",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L538-L541",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L538-L541)
- Source range: L538-L541
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Both neutrino and charged-lepton σ-polarity matrices are σ-symmetric tridiagonal,
    so they share the same eigenvector structure:
      v_σ-odd  = [1, 0, -1]/√2  (exact for ALL such matrices)
      v_σ-even determined by (a-c) and b
    Therefore: PMNS = V_ℓ† · V_ν ≈ identity from σ-structure alone.
    Physical consequence: σ-polarity generates mass eigenstates; flavor mixing (PMNS)
    requires additional A-sector rotation (Sprint 5).
    If V_ℓ = identity: θ₁₃=9.85° (PDG 8.57°, +15%), θ₁₂=45.86°, θ₂₃=80.01°. -/
```

## Source Excerpt

```lean
def pmns_mixing_angles : String :=
  "PMNS from σ-matrix alone ≈ identity (shared eigenvector structure). " ++
  "If V_ℓ=id: θ₁₃=9.85° (PDG 8.57°, +15%), θ₁₂=45.86° (PDG 33.4°, fails). " ++
  "Full PMNS requires A-sector flavor rotation (Sprint 5)."
```
